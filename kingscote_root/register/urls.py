from django.urls import path

from . import views
from .views import StudentList, StudentView

urlpatterns = [
    # path('/', views.index, {'pagename': ''}, name='home'),
    path('', views.student_reg, name='student-register-request'),
    path('show/<int:pk>', StudentView.as_view(), name='student-detail'),
    path('show', StudentList.as_view(), name='show-quotes'),
]