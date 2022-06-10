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
from acatdog.views.register import PlayerView
from acatdog.views.userinfoselfchge import UserInfoSelfChge
from acatdog.views.savehelpfrom import SaveAssist
from acatdog.views.saveadoption import SaveAdopt
from acatdog.views.selectsix import AniList
from acatdog.views.selectphoto import AdoList
from acatdog.views.selectone import AniOne
from acatdog.views.selectadopt import AdoOne
from acatdog.views.selectmyadopt import AdoptList
from acatdog.views.selectassist import AssOne
from acatdog.views.changepwd import ChangePwd
from acatdog.views.adoptsuccess import AdoSuccess
from acatdog.views.adoptfail import AdoFail
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
    path('getinfo/', GetInfo.as_view(), name="getinfo"),
    path('register/', PlayerView.as_view(), name="register"),
    path('saveassit/', SaveAssist.as_view(), name="saveassit"),
    path('anilist/', AniList.as_view(), name="anilist"),
    path('photolist/', AdoList.as_view(), name="photolist"),
    path('anione/', AniOne.as_view(), name="anione"),
    path('adoone/', AdoOne.as_view(), name="adoone"),
    path('assone/', AssOne.as_view(), name="assone"),
    path('selectadopt/', AdoptList.as_view(), name="selectadopt"),
    path('adosucc/', AdoSuccess.as_view(), name="adosucc"),
    path('adofail/', AdoFail.as_view(), name="adofail"),
    path('userinfoselfchge/', UserInfoSelfChge.as_view(), name="userinfoselfchge"),
    path('saveadopt/', SaveAdopt.as_view(), name="saveadopt"),
    path('changepwdapi/', ChangePwd.as_view(), name="changepwd"),
]
