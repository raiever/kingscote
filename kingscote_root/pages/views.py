from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1> Kingscote Homepage </h1>")
    return render(request, 'base.html')

# Create your views here.
