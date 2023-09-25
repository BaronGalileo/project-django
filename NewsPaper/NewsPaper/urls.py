from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('page/', include('django.contrib.flatpages.urls')),
   path('news/', include('news.urls')),
]