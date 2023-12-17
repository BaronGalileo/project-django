from django.contrib.auth import login
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('cat/', CategoryList.as_view(), name='category'),
    path('messages/', views.message, name="messages"),
    path('create/', views.create, name="create"),
    path('post/<int:pk>', PostDetail.as_view(), name="post"),
    path('post/<int:pk>', CommentCreate, name="comment"),

    ]