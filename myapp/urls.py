from django.urls import path

from . import views
from myapp.views import video_list, video_detail, user_register, user_login, \
    user_logout, mypage, video_create, avatar_upload, like_video, unlike_video, \
    video_update, video_delete


urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:id>/', video_detail, name='video_detail'),
    path('videos/<int:id>/update/', video_update, name='video_update'),
    path('videos/<int:id>/delete/', video_delete, name='video_delete'),
    path('videos/create/', video_create, name='video_create'),
    path('videos/like_video/', like_video, name='like_video'),
    path('videos/unlike_video/', unlike_video, name='unlike_video'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('mypage/', mypage, name='mypage'),
    path('avatar-upload/', avatar_upload, name='avatar_upload'),
]
