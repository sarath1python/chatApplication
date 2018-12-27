from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login, name = "login"),
    # path('<int: userId>',views.chatClass , name='chat')
]