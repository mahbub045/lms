from django.shortcuts import render
from .models import Post


def adminpage(request):
    return render(request, 'lms/adminpage.html',)

def teacher(request):
    return render(request, 'lms/teacher.html',)

def student(request):
    return render(request, 'lms/student.html',)