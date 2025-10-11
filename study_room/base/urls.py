from django.urls import path
from . import views 


urlpatterns = [
   
    path('register/', views.registerUser,name="register"),
    path('login/', views.loginPage,name="login"),
    path('logout/', views.logoutPage,name="logout"),
    path('', views.home,name="home"),  # Empty path for root URL, calls home function
    path('room/<int:pk>/', views.room, name="room"),
    path('navbar/', views.navbar,name="navbar"),
    path('create-room/', views.createroom,name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom,name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage,name="delete-message"),
]