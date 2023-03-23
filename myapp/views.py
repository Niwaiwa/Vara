from django.shortcuts import render

from django.http import HttpResponse
from .models import Video


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'myapp/video_list.html', {'videos': videos})