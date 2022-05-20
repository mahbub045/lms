from django.shortcuts import render
from .models import Post


def teacher(request):
    return render(request, 'lms/teacher.html',)
