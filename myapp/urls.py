
from django.urls import path

from . import views, chat

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello1/', views.hello1, name='hello1'),
    path('myViewGet', views.my_view, name='myViewGet'),
    path('myViewPost', views.my_view_post, name='myViewPost'),

    path('chat01',chat.chat01)
]