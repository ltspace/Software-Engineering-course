"""pcatdog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import imp
import sys
import os
# os.chdir(os.path.dirname(__file__))
# sys.path.append("..")
# from ..acatdog.urls import urls as login
from acatdog.views.getInfo import GetInfo
from django.urls import path, include
from re import template
from tempfile import tempdir
from django import urls
from django.contrib import admin
from django.db import router
from django.views.generic import TemplateView
from rest_framework import routers




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('api/', include('acatdog.urls.urls')),
    path('getinfo/', GetInfo.as_view(), name="myspace_getinfo"),
]

