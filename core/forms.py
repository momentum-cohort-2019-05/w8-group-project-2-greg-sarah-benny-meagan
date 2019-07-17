from django import forms

from core.models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body',)
