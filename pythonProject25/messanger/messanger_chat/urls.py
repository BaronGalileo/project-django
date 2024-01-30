from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *

urlpatterns = [
    path('', ProfileList.as_view(), name='home'),
    path('test/', views.index, name='test'),
    path('room/<int:pk>', RoomDetail.as_view(), name='room'),
    path('register', RegisterView.as_view(), name="register"),
    path('addroom', views.create, name='add_room'),
    path('profile/<int:pk>', AccauntDetail.as_view(), name='profile'),
    path('addprofile', AccauntCreate.as_view(), name='addprofile'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)