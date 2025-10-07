from django.urls import path
from . import views 


urlpatterns = [
   
    path('', views.home,name="home"),  # Empty path for root URL, calls home function
    path('room/<int:pk>/', views.room, name="room"),
    path('navbar/', views.navbar,name="navbar"),
    path('create-room/', views.createroom,name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom,name="update-room"),
]