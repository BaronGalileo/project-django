from django.urls import path
from . import views
from .views import *




urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('cat/', CategoryList.as_view(), name='category'),
    path('messages/', MyPostList.as_view(), name="messages"),
    path('create/', views.create, name="create"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post"),
    path('post/<int:pk>/update', PostUpdateDetail.as_view(), name="post-update"),
    path('post/<int:pk>/delete', PostDeleteDetail.as_view(), name="post-delete"),
    path('comment/<int:pk>', CommentDelete.as_view(), name="comment-delete"),
    path('comment/<int:pk>/response', CommentResponse.as_view(), name="comment-response"),
    path('comments/', CommentList.as_view(), name="comments"),
    path('comments/<int:pk>', CommentList.as_view(), name="comment"),
]
