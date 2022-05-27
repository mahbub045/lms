from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Post


def adminpage(request):
    return render(request, 'lms/adminpage.html')

def teacher(request):
    return render(request, 'lms/teacher.html')

def view_T_course(request):
    return render(request, 'lms/view_T_course.html',)

def student(request):
    return render(request, 'lms/student.html')



def signin(request):
	if request.method == 'GET':
		return render(request, 'lms/login.html')
	elif request.method == 'POST':
		u = request.POST.get('user')
		p = request.POST.get('pass')
		user = authenticate(username=u, password=p)
		if user is None:
			return render(request, 'lms/login.html')
		else:
			login(request, user)
			return redirect('admin_page')

def teacher_signin(request):
	if request.method == 'GET':
		return render(request, 'lms/login.html')
	elif request.method == 'POST':
		u = request.POST.get('user')
		p = request.POST.get('pass')
		user = authenticate(username=u, password=p)
		if user is None:
			return render(request, 'lms/login.html')
		else:
			login(request, user)
			return redirect('teacherpage')