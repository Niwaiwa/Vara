import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from .models import Video, Tag, UserAvatar
from .forms import VideoCreateForm, AvatarUploadForm


def index(request):
    return redirect('/myapp/videos/')

@login_required(login_url='/myapp/login/')
def video_create(request):
    if request.method == 'POST':
        form = VideoCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title: str = form.cleaned_data['title']
            description: str = form.cleaned_data['description']
            url: str = form.cleaned_data['url']
            tags: str = form.cleaned_data['tags']
            video_file = ""
            if request.FILES.get('video_file'):
                video_file = request.FILES['video_file']
            user = request.user
            video = Video.objects.create(title=title, description=description, url=url, video_file=video_file, user=user)
            if tags:
                tag_names = [name.strip() for name in tags.split(',')]
                existed_tags = Tag.objects.filter(name__in=tag_names)
                new_tags = set(tag_names) - set(existed_tags.values_list('name', flat=True))
                tag_obj_set = (Tag(name=tag) for tag in new_tags)
                tag_objs = Tag.objects.bulk_create(tag_obj_set)
                video.tags.add(*tag_objs, *existed_tags)
            return redirect(f'/myapp/videos/{video.pk}/')
        return render(request, 'myapp/video_create.html', {'form': form})
    else:
        return render(request, 'myapp/video_create.html')

@login_required(login_url='/myapp/login/')
def video_update(request, id):
    video = get_object_or_404(Video, pk=id)
    if request.method == 'POST':
        video.title = request.POST['title']
        video.description = request.POST['description']
        tags = request.POST['tags']
        if tags:
            tag_names = [name.strip() for name in tags.split(',')]
            existed_tags = Tag.objects.filter(name__in=tag_names)
            new_tags = set(tag_names) - set(existed_tags.values_list('name', flat=True))
            tag_obj_set = (Tag(name=tag) for tag in new_tags)
            tag_objs = Tag.objects.bulk_create(tag_obj_set)
            if video.tags != existed_tags:
                video.tags.clear()
                video.tags.add(*tag_obj_set, *existed_tags)
        else:
            video.tags.clear()
        video.url = request.POST['url']
        if request.FILES.get('video_file'):
            video.video_file = request.FILES['video_file']
        video.save()
        return redirect(f'/myapp/videos/{video.pk}/')
    context = {'video': video}
    return render(request, 'myapp/video_update.html', context)

@login_required(login_url='/myapp/login/')
@require_POST
def video_delete(request ,id):
    video = get_object_or_404(Video, id=id)
    video.delete()
    return redirect('/myapp/videos/')

def video_list(request):
    tag = request.GET.get('tag')
    if tag:
        tag = Tag.objects.get(name=tag)
        videos = tag.taged_videos.all()
    else:
        videos = Video.objects.all()
    return render(request, 'myapp/video_list.html', {'videos': videos})

def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    # print(video.user.useravatar.avatar.url)
    return render(request, 'myapp/video_detail.html', {'video': video})

@require_POST
def like_video(request):
    video_id = request.POST.get('video_id')
    video = get_object_or_404(Video, id=video_id)
    video.likes.add(request.user)
    return redirect(f'/myapp/videos/{video_id}/')

@require_POST
def unlike_video(request):
    video_id = request.POST.get('video_id')
    video = get_object_or_404(Video, id=video_id)
    video.likes.remove(request.user)
    return redirect(f'/myapp/videos/{video_id}/')

def user_register(request):
    if request.method == 'POST':
        uname: str = request.POST.get('username')
        pwd: str = request.POST.get('password')
        email: str = request.POST.get('email')
        if User.objects.filter(username=uname).count() > 0:
            return HttpResponse('Username already exists.')
        else:
            _ = User.objects.create_user(uname, email, pwd)
            return redirect('login')
    else:
        return render(request, 'myapp/register.html')

def user_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        check_user = authenticate(request, username=uname, password=pwd)
        if check_user:
            login(request, check_user)
            return redirect('/myapp/videos/')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'myapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/myapp/login/')
def mypage(request):
    user = request.user
    try:
        user_avatar = UserAvatar.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        user_avatar = None
    return render(request, 'myapp/mypage.html', {'user': user, 'user_avatar': user_avatar})

@login_required(login_url='/myapp/login/')
def avatar_upload(request):
    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            try:
                user_avatar = UserAvatar.objects.get(user_id=user.id)
                user_avatar.avatar = form.cleaned_data['file']
                user_avatar.save()
            except ObjectDoesNotExist:
                user_avatar = UserAvatar.objects.create(user=user, avatar=form.cleaned_data['file'])
            return redirect('/myapp/mypage/')
        else:
            return render(request, 'myapp/avatar_upload.html', {'form': form})
    else:
        return render(request, 'myapp/avatar_upload.html')
