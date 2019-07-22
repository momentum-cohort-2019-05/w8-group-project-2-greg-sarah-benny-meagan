from django import forms

from core.models import Question

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ('title', 'body', 'categories', 'user',)


# class AnswerForm(forms.ModelForm):
#     model = Answer
#     fields = ('title', 'categories')