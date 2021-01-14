"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from gamestore.views import index, article_1, article_2, user_article, article_number,users_number_article,phone, mark

urlpatterns = [
    path('first_page', include('gamestore.urls')),
    path('', index, name='index'),
    path('articles/', article_1, name='first_article'),
    path('acrticles/archive/', article_2, name='archive_article'),
    path('users/', user_article, name='users_article'),
    path('article/<int:article_id>/', article_number, name='article'),
    path('article/<int:article_id>/<slug:slug_text>', article_number, name='article_text'),
    path('users/<int:article_id>', users_number_article, name='users id'),
    re_path(r'^(?P<phone_number>0{1}\d{9}$)', phone, name='phone number'),
    re_path(r'^(?P<mark_text>^[0-9a-f]{4}\-{1}[0-9a-z]{6}$)', mark, name='marks'),
]
