from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect
from django import forms
from core.models import Question, Answer, Category
from core.forms import QuestionForm, AnswerForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from core import views
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
    
   
    # def answer_form(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            
    else:
        form = AnswerForm()
    
    return render(request, 'detail.html', {'form': form, 'question': question})


def mark_answer_correct(request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        answer.correct = True

def questions_by_category(request, category_pk):
    questions_by_category = Question.objects.filter(categories__pk=category_pk)
    category = get_object_or_404(Category, pk=category_pk)

    context = {
        'questions_by_category': questions_by_category,
        'category': category,
    }

    return render(request, 'questions_by_category.html', context)

def liked_content(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    answer.liked += 1
    answer.save()
    return JsonResponse({'likes':answer.liked})

@login_required
def question_form(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = QuestionForm()
    return render(request, 'question_form.html', {'form': form})