from django.urls import path

from . import views
from myapp.views import video_list, video_detail, tag_detail, user_register, user_login, user_logout, mypage, video_create


urlpatterns = [
    path('', views.index, name='index'),
    path('videos/create/', video_create, name='video_create'),
    path('videos/', video_list, name='video_list'),
    path('videos/<int:id>/', video_detail, name='video_detail'),
    path('tags/<int:id>/', tag_detail, name='tag_detail'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('mypage/', mypage, name='mypage'),
]
