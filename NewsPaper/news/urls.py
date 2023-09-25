from django.urls import path


from .views import PostList, PostDetail, PostCreate, MyViev, ArticlesCreate, PostUpdate, ArticlesUpdate, PostDelete, \
   ArticlesDelete

urlpatterns = [

   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', MyViev.as_view(), name='post_list_fil'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('articles/create/', ArticlesCreate.as_view(), name='ar_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('articles/<int:pk>/edit/', ArticlesUpdate.as_view(), name='ar_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='ar_delete'),
]