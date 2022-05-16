from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#create your models here
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	data_posted = models.DateTimeField(default=timezone.now)

	#auto_now = True or auto_now_add=True
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
	content = models.TextField()
	which_post = models.ForeignKey(Post, on_delete=models.CASCADE)