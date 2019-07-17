from django.shortcuts import render

from core.models import Question, Answer

# Create your views here.

def index(request):
    """View function for home page of site."""

    question = Question.objects.all()
        
    context = {
        'question': question,
    }
    return render(request, 'index.html', context=context)

    