from django.shortcuts import render, get_object_or_404, get_list_or_404

from django.http import HttpResponse
from .models import Video, Tag, TagVideo


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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