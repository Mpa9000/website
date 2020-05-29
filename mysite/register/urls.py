from django.urls import path

from . import views

urlpatterns = [
    path('', views.entrar, name='entrar'),
    path('register', views.register, name='register'),
    path('login', views.entrar, name='singin'),
    path('logout', views.logoutUser, name='logout'),
]