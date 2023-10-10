
from django.contrib import admin
from django.urls import path ,include
from . import views


urlpatterns = [
    path('login/', views.loginUser ,name="login"),
    path('logout/', views.logoutUser ,name="logout"),
    path('register/', views.registerUser ,name="register"),
    

    path('', views.home ,name="home"),
    path('room/<int:pk>/', views.room ,name="room"),
    path('create_room/', views.createRoom ,name="create_room"),
    path('update_room/<int:pk>/', views.updateRoom ,name="update_room"),
    path('delete_room/<int:pk>/', views.deleteRoom ,name="delete_room"),


    
]
