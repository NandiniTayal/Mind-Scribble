from django.shortcuts import render
from .models import Quiz

def index(request):
	quiz_list=Quiz.objects.all()
	context= {'quiz_list':quiz_list}
	return render(request,'quiz/index.html',context)
# Create your views here.
