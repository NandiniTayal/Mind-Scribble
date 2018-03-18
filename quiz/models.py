from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	choice_text = models.CharField(max_length=1)
	answer_id = models.IntegerField()
	quiz= models.ForeignKey('Quiz',on_delete=models.CASCADE,)

class Quiz(models.Model):
	title =models.CharField(max_length = 50)
	desc=models.CharField(max_length=200)

# Create your models here.
