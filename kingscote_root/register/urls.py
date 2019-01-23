from django.urls import path

from . import views
from .views import StudentList

urlpatterns = [
    path('', views.student_reg, name='student-register-request'),
    path('show', StudentList.as_view(), name='show-quotes'),
]