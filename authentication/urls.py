from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('',views.login, name = "login"),
    path('validate_user/', views.authentication, name="authentication"),
    path('create_user/',views.createUser, name="create_user")
]