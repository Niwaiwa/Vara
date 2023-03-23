from django.urls import path

from . import views
from myapp.views import video_list


urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', video_list, name='video_list'),
]