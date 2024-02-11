from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from instructor.models import Article, Quiz, QuizAnswar
from account.models import LearnerProfile, InstructorProfile
from .forms import AskQuestionForm, AnswarQuestionForm
from .models import AskedQuestion, AnswarQuestion

# Create your views here.

def home(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'learner/home.html', context={'articles': articles})


@login_required
def article_details(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'learner/article_details.html', context={'article': article})


@login_required
def quiz(request):
    allquiz = Quiz.objects.all().order_by('-id')
    dic = {
        'allquiz': allquiz
    }
    for quiz in allquiz:
        ans = QuizAnswar.objects.filter(user=request.user, quiz=quiz)

        if ans.exists():
            dic.update({'answar': True})
        else:
            dic.update({'answar': False})

    return render(request, 'learner/quiz.html', context={'allquiz': allquiz})


@login_required
def answar(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        answar = request.POST.get('answar')
        if quiz.correct_ans == answar:
            quiz_ans = QuizAnswar.objects.get_or_create(
                user=request.user, quiz=quiz)
            if quiz_ans[1]:
                messages.success(request, 'Right Answar !')
            else:
                messages.info(request, 'You Allready Gave this Answar !')
        else:
            messages.warning(request, 'wrong ans Try again !')

    return HttpResponseRedirect(reverse('quiz'))


@login_required
def ask_question(request):
    learner = LearnerProfile.objects.filter(user=request.user)
    form = AskQuestionForm()
    if learner.exists():
        if learner[0].is_fully_filled():
            if request.method == 'POST':
                form = AskQuestionForm(request.POST)
                if form.is_valid():
                    askedquestionform = form.save(commit=False)
                    askedquestionform.learner = learner[0]
                    askedquestionform.save()
                    form = AskQuestionForm()
                    return HttpResponseRedirect(reverse('forum'))
        else:
            messages.warning(request, 'Please Fill Your Profile Info First !')
            return HttpResponseRedirect(reverse('profile'))
    else:
        messages.warning(request, 'Only Student Can be Ask question !')
    return render(request, 'learner/ask_question.html', context={'form': form})


def show_question(request):
    allquestion = AskedQuestion.objects.all().order_by('-id')

    return render(request, 'learner/forum.html', context={'allquestion': allquestion})


@login_required
def answar_question(request, pk):
    question = AskedQuestion.objects.get(pk=pk)
    answars = AnswarQuestion.objects.filter(question=question)
    instructor = InstructorProfile.objects.filter(user=request.user)
    if instructor.exists:
        form = AnswarQuestionForm()
        if request.method == 'POST':
            form = AnswarQuestionForm(request.POST)
            if form.is_valid():
                ansquestionform = form.save(commit=False)
                ansquestionform.instructor = instructor[0]
                ansquestionform.question = question
                ansquestionform.save()
                return HttpResponseRedirect(reverse('App_learner:question_details', kwargs={'pk': question.pk}))

    return render(request, 'learner/question_details.html', context={'question': question, 'form': form, 'answars': answars})