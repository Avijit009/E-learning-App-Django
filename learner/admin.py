from django.contrib import admin
from .models import AnswerQuestion, AskedQuestion
# Register your models here.


@admin.register(AskedQuestion)
class AskedQuestionAdmin(admin.ModelAdmin):
    '''Admin View for AskedQuestion'''

    list_display = ('id', 'learner', 'subject', 'description')
    list_per_page = 10


@admin.register(AnswerQuestion)
class AnswerQuestionAdmin(admin.ModelAdmin):
    '''Admin View for AnswarQuestion'''

    list_display = ('id', 'instructor', 'question', 'answer')