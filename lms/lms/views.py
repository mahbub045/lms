from django.shortcuts import render
from .models import Post


def home(request):
	all_post = Post.objects.all().order_by('-data_posted')
    return render(request, 'lms/index.html', {'all' : all_post})
