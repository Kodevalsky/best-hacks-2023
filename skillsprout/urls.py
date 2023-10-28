"""
URL configuration for skillsprout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #Krzysztofowe
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('about_us/', views.about_us, name="about_us"),
    path('offers/', views.offers, name="offers"),
    path('single_offer/', views.single_offer, name="single_offer"),
    path('your_visits/', views.your_visits, name="your_visits"),
    path('single_visit/', views.single_visit, name="single_visit"),

]
