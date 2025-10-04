from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL (unchanged)
    path('', include('base.urls')),
    
]