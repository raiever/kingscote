from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('class', views.class_timetable, name='class_timetable'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.index, name='index'),
]