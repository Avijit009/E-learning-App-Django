from django.forms import ModelForm
from .models import Article, Quiz


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['author']


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        exclude = ['instructor']