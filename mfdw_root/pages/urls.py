from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, {'pagename': ''}, name='home'),  #path(route, view), pagename: '' is mentioned for home specially.
    path('contact', views.contact, name='contact'),
    path('class', views.class_table, name='class_table'), 
    path('<str:pagename>', views.index, name='index'),
]


