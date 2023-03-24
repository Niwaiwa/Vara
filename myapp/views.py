from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import Video, Tag
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
    else:
        param = {}
    videos = Video.objects.all()
    return render(request, 'base.html', param.update({'videos': videos}))
    
def video_list(request):
    videos = Video.objects.all()
    return render(request, 'myapp/video_list.html', {'videos': videos})

def video_detail(request, id):
    video = get_object_or_404(Video, id=id)
    tags = Tag.objects.filter(tagvideo__video_id=id)
    print(tags)
    return render(request, 'myapp/video_detail.html', {'video': video, 'tags': tags})

def tag_detail(request, id):
    tag = get_object_or_404(Tag, id=id)
    videos = Video.objects.filter(tagvideo__tag_id=id)
    return render(request, 'myapp/tag_detail.html', {'videos': videos, 'tag': tag})

def user_register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        email = request.POST.get('email')
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
    return render(request, 'myapp/mypage.html', {'user': user})