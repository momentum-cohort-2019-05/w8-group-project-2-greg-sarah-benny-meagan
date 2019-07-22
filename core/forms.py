from django import forms

from core.models import Question, Answer

class QuestionForm(forms.ModelForm):
    
    class Meta:
        model = Question
        fields = ('title', 'body', 'categories',)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('body',)