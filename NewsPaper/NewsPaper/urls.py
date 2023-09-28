from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('page/', include('django.contrib.flatpages.urls')),
   path("accounts/", include("allauth.urls")),
   # path('accounts/', include('django.contrib.auth.urls')),
   # path("accounts/", include("accounts.urls")),
   path('home/', include('news.urls')),
]