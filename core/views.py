from django.shortcuts import render
from core.models import Question
from core.forms import QuestionForm
import django.contrib.auth.decorators 


# Create your views here.

def index(request):
    questions = Question.objects.all()

    context = {
        'questions': question
    }
    
    return render(request, 'index.html', context)


def question(request):
    question = Question.objects.all()

    context = {
        'question': question
    }

    return render(request, 'core/question', context)



