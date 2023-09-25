from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('page/', include('django.contrib.flatpages.urls')),
   path('home/', include('news.urls')),
]