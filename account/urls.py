from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.edit_profile, name='profile'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('change_password/', views.change_password, name='change_password')
]