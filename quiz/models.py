from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	choice_text = models.TextField()
	answer_id = models.IntegerField()
	quiz= models.ForeignKey('Quiz',on_delete=models.CASCADE,)

	def __str__(self):
		txt = self.question_text
		if len(txt) > 50:
			return txt[:50] + '...' 
		else:
			return txt

class Quiz(models.Model):
	title =models.CharField(max_length = 50)
	desc=models.CharField(max_length=200)

	def __str__(self):
		return self.title


