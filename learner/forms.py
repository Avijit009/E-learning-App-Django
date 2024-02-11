from django import forms
from .models import AskedQuestion, AnswerQuestion


class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = AskedQuestion
        exclude = ['learner']


class AnswerQuestionForm(forms.ModelForm):
    class Meta:
        model = AnswerQuestion
        exclude = ['instructor', 'question']