from django.shortcuts import render
from .models import Post


def adminpage(request):
    return render(request, 'lms/adminpage.html')

def teacher(request):
    return render(request, 'lms/teacher.html')

def view_T_course(request):
    return render(request, 'lms/view_T_course.html')

def student(request):
    return render(request, 'lms/student.html')


def login(request):
    return render(request, 'lms/login.html')