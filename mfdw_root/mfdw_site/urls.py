"""mfdw_site URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from quotes.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name ='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('quote/', include('quotes.urls')),
    path('', include('django.contrib.auth.urls')),  #auth.urls has path(/login)
    path('', include('pages.urls')),
]


