from django import forms
from django.forms import ModelForm
from .models import Student


class StudentForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Student
        fields = [
            'name', 'address', 'mobile', 'email', 'age', 'country',
            'en_level', 'attached_files'
        ]