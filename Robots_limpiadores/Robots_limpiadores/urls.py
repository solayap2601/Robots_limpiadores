"""Robots_limpiadores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sitio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/plataforma/', views.login_plataforma, name='login_plataforma'),
    path('register/robot/', views.robot_registration, name='robot_registration'),
    path('register/habitacion/', views.Habita_registration, name='Habita_registration'),
    path('mostrar', views.mostrar_robot, name='mostrar_robot'),
    path('carga', views.mandar_estacion,name='mandar_estacion'),
    path('admin/', admin.site.urls),
    
]
