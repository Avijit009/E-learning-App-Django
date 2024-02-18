from django.contrib import admin
from .models import Article, Quiz, QuizAnswer, Category

# Register your models here.


@admin.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('id', 'name', 'created_at')
    list_per_page = 10


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    '''Admin View for Article'''

    list_display = ('id', 'title', 'published_at', 'updated_at')
    list_per_page = 10


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    '''Admin View for Quiz'''

    list_display = ('id', 'instructor', 'quiz_question', 'option_1',
                    'option_2', 'option_3', 'option_4', 'correct_ans')
    list_per_page = 10


@admin.register(QuizAnswer)
class QuizAnswerAdmin(admin.ModelAdmin):
    '''Admin View for QuizAnswer'''

    list_display = ('id', 'user', 'quiz')