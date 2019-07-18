from django import forms

from core.models import Question, Answer

class QuestionForm(forms.ModelForm):
    model = Question
    fields = ('title', 'body', 'categories')


class AnswerForm(forms.ModelForm):
    model = Answer
    fields = ('title', 'categories')
