from django.urls import path
from . import views

urlpatterns = [
    path('Home', views.Home, name='Home'),
    path('InicioSesion', views.InicioSesion, name='InicioSesion'),
    path('Registro', views.Registro, name='Registro'),
    path('Api', views.Api, name='Api')
]