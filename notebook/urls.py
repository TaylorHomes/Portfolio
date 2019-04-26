"""notebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from core import views
from django.urls import path
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('illustration/',
         TemplateView.as_view(template_name='illustration.html'),
         name='illustration'),
    path('development/',
         TemplateView.as_view(template_name='development.html'),
         name='development'),
    path('about/',
         TemplateView.as_view(template_name='about.html'),
         name='about'),
    path('resume/',
         TemplateView.as_view(template_name='resume.html'),
         name='resume'),
    path('spotswood/',
         TemplateView.as_view(template_name='spotswood.html'),
         name='spotswood'),
    path('kaiketsu/',
         TemplateView.as_view(template_name='kaiketsu.html'),
         name='kaiketsu'),
    path('decreedly/',
         TemplateView.as_view(template_name='decreedly.html'),
         name='decreedly'),
    path('react/',
         TemplateView.as_view(template_name='react.html'),
         name='react'),
]
