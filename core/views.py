from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from core.models import Question, Answer, Category
from core.forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from core import views
# import django.contrib.auth.decorators
# from django.contrib.auth.decorators import login_required

def index(request):
    """View function for home page of site, which includes a list of all questions."""

    question_list = Question.objects.all()
    # category_name = get_object_or_404(Category, category_name='Species')
        
    context = {
        'question_list': question_list,
        # 'category_name': category_name,
    }    
    return render(request, 'index.html', context)

def question_detail(request, pk):
    """Individual question pages, which includes all answers to a given question."""

    question = get_object_or_404(Question, pk=pk)

    return render(request, 'detail.html', {'question':question})

def questions_by_category(request, category_pk):
    questions_by_category = Question.objects.filter(categories__pk=category_pk)
    category = get_object_or_404(Category, pk=category_pk)

    context = {
        'questions_by_category': questions_by_category,
        'category': category,
    }

    return render(request, 'questions_by_category.html', context)

def question_form(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = QuestionForm()
        # args = {'form': form}
    return render(request, 'question_form.html', {'form': form})