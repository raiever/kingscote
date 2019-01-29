from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Student
from .forms import StudentForm
from pages.models import Page

class StudentList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    # model = Student
    context_object_name = 'all_students'

    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

    def get_queryset(self):
        return Student.objects.filter(username=self.request.user)


class StudentView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    # model = Student
    context_object_name = 'student_detail'

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context
    
    def get_queryset(self):
        return Student.objects.filter(username=self.request.user)


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)

@login_required(login_url=reverse_lazy('login'))
def student_reg(request):
    submitted = False
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        
        if form.is_valid():
            student = form.save(commit=False)
            try:
                student.username = request.user
            except Exception:
                pass
            student.save()
            return HttpResponseRedirect('/register_class/?submitted=True')
    else:
        form = StudentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'register/class_register.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)

# Create your views here.
