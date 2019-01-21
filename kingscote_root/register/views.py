from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Student
from .forms import StudentForm
from pages.models import Page

def student_reg(request):
    submitted = False
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/?submitted=True')
    else:
        form = StudentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register/student.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})

# Create your views here.
