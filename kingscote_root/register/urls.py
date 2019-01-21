from django.urls import path

from . import views

urlpatterns = [
    path('', views.student_reg, name='student-register-request'),
]