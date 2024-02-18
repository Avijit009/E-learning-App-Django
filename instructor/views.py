from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from account.models import InstructorProfile
from .models import Article, Quiz
from .forms import ArticleForm, QuizForm

# Create your views here.

@login_required
def write_article(request):
    form = ArticleForm()
    instructor = InstructorProfile.objects.filter(user=request.user)
    print(instructor)
    if instructor.exists():
        if instructor[0].is_fully_filled():

            if request.method == 'POST':
                form = ArticleForm(request.POST, request.FILES)
                if form.is_valid():
                    article_form = form.save(commit=False)
                    article_form.author = instructor[0]
                    article_form.save()
                    messages.success(
                        request, 'Your Article Posted successfully !')
                    form = ArticleForm()
                    return HttpResponseRedirect(reverse('home'))
                else:
                    messages.warning(
                        request, 'Something went Wrong! please try again!')
        else:
            messages.warning(request, 'Please Fill Your Profile Information First !')
            return HttpResponseRedirect(reverse('profile'))

    else:
        messages.warning(request, 'Only Instructor Can Post Article !')
    return render(request, 'instructor/post_article.html', context={'form': form, 'heading': 'Post Article', 'btn_name': 'Post'})

@login_required
def my_article(request):
    instructor = InstructorProfile.objects.filter(user=request.user)
    if instructor.exists():
        articles = Article.objects.filter(author=instructor[0])
    else:
        messages.warning(request, 'You Are not an Instructor !')

    return render(request, 'instructor/my_article.html', context={'articles': articles})

@login_required
def edit_article(request, pk):
    artical = Article.objects.get(pk=pk)
    instructor = InstructorProfile.objects.filter(user=request.user)
    if instructor.exists():
        form = ArticleForm(instance=artical)
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=artical)
            article_form = form.save(commit=False)
            article_form.author = instructor[0]
            article_form.save()
            messages.success(request, 'Saved Successfully !')
            return HttpResponseRedirect(reverse('my_article'))
    else:
        messages.warning(request, 'You Are not Our Instructor !')
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'instructor/post_article.html', context={'form': form, 'heading': 'Edit Article', 'btn_name': 'Update'})


@login_required
def delete_article(request, pk):
    artical = Article.objects.get(pk=pk)
    artical.delete()
    messages.info(request, 'Deleted Successfully !')
    return HttpResponseRedirect(reverse('my_article'))

@login_required
def post_quiz(request):
    form = QuizForm()
    instructor = InstructorProfile.objects.filter(user=request.user)
    if instructor.exists():
        if instructor[0].is_fully_filled():

            if request.method == 'POST':
                form = QuizForm(data=request.POST)
                if form.is_valid():
                    quiz_form = form.save(commit=False)
                    quiz_form.instructor = instructor[0]
                    quiz_form.save()
                    messages.info(request, 'Quiz Added!')
                    form = QuizForm()
                    return HttpResponseRedirect(reverse('quiz'))
        else:
            messages.warning(request, 'Please Fill Your Profile Information First !')
            return HttpResponseRedirect(reverse('profile'))

    else:
        messages.warning(request, 'Only a instructor can post a quiz!')

    return render(request, 'instructor/quiz_form.html', context={'form': form})