from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('article_details/<pk>/', views.article_details, name='article_details'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_ans/<pk>/', views.answer, name='quiz_ans'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('forum/', views.show_question, name='forum'),
    path('question_details/<pk>/', views.answer_question, name='question_details')
]