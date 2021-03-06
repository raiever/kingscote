"""kingscote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView
from register.views import Register

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('admin/', admin.site.urls),
    path('register_user/success/', TemplateView.as_view(template_name="registration/success.html"), name='register-success'),
    path('register_user/', Register.as_view(), name='register'),
    path('register_class/', include('register.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
]
