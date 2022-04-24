from django.contrib import admin
from django.urls import path, include
from .main import home

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls), 
    path('auth/', include('authentication.urls')),
    path('supportdesk/', include('supportdesk.urls')),
]