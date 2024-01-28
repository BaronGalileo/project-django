from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import RoomList, RegisterView, RoomDetail

urlpatterns = [
    path('', RoomList.as_view(), name='home'),
    path('test/', views.index, name='test'),
    path('room/<int:pk>/', RoomDetail.as_view(), name='room'),
    path('register', RegisterView.as_view(), name="register"),
    path('addroom', views.create, name='add_room'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)