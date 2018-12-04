from django.shortcuts import render

# Create your views here.
def index(request):
    # name = 'SungHwan Kim'
    # age = 36
    # mobile = 1234
    # context = {'student_name': name,
    #            'student_age': age,
    #            'student_mobile': mobile}
    return render(request, 'index.html', {'students': students})

class Student:
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

students = [
    Student('SungHwan Kim', 36, 1234),
    Student('Ana', 21, 5678),
    Student('Sara', 19, 9012)
]