"""shopping URL Configuration

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
from . import views
from django.urls import path, include
from .views import delete_stuff
from .views import search_view
app_name='mall'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:stuff_id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('info/', views.info, name='info'),
    path('logout/', views.logout_view, name='logout'),
    path('stuff/<int:stuff_id>/toggle_like/', views.toggle_like, name='toggle_like'),
    path('my_likes/', views.my_likes, name='my_likes'),
    path('delete/<int:stuff_id>/', delete_stuff, name='delete_stuff'),
    path('<int:stuff_id>/update/', views.update_stuff, name='update_stuff'),
    path('search/', views.search_results, name='search_results'),
]