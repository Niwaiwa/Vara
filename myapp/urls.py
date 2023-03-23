from django.urls import path

from . import views
from myapp.views import video_list, video_detail, tag_detail


urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:id>/', video_detail, name='video_detail'),
    path('tags/<int:id>/', tag_detail, name='tag_detail'),
]
