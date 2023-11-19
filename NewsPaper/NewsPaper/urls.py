from django.contrib import admin
from django.urls import path, include

from news.views import login_view

urlpatterns = [
   path('admin/', admin.site.urls),
   path('page/', include('django.contrib.flatpages.urls')),
   path("accounts/", include("allauth.urls")),
   # path('accounts/', include('django.contrib.auth.urls')),
   # path("accounts/", include("accounts.urls")),
   path('home/', include('news.urls')),
   path('test/login', login_view,),
]