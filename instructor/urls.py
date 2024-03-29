from django.urls import path
from . import views

urlpatterns = [
    path('write_article/', views.write_article, name='write_article'),
    path('my_article/', views.my_article, name='my_article'),
    path('edit_article/<pk>/', views.edit_article, name='edit_article'),
    path('delete_article/<pk>/', views.delete_article, name='delete_article'),
    path('post_quiz/', views.post_quiz, name='post_quiz'),
]