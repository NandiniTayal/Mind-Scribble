from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz

class UserInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	quiz = models.ManyToManyField(Quiz)

	def __str__(self):
		return self.user.username
