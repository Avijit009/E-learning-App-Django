from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

from .models import InstructorProfile, LearnerProfile
from .forms import SignUpForm, InstructorProfileForm, LearnerProfileForm

# Create your views here.


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully !')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'account/register.html', context={'form': form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully Logged in !')
                return HttpResponseRedirect(reverse('home'))

    return render(request, 'account/login.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully !')
    return HttpResponseRedirect(reverse('login'))


@login_required
def update_profile(request):
    learner_profile = InstructorProfile.objects.filter(user=request.user)
    instructor_profile = LearnerProfile.objects.filter(user=request.user)

    if learner_profile.exists():
        form = LearnerProfileForm(instance=learner_profile[0])
        if request.method == 'POST':
            form = LearnerProfileForm(
                request.POST, request.FILES, instance=learner_profile[0])
        if form.is_valid():
            learner_form = form.save(commit=False)
            learner_form.user = request.user
            learner_form.save()
            messages.success(request, 'Profile Saved Successfully !')
            form = LearnerProfileForm(instance=learner_profile[0])

    else:
        form = InstructorProfileForm(instance=instructor_profile[0])
        if request.method == 'POST':
            form = InstructorProfileForm(
                request.POST, request.FILES, instance=instructor_profile[0])
            if form.is_valid():
                instructor_form = form.save(commit=False)
                instructor_form.user = request.user
                instructor_form.save()
                form = InstructorProfileForm(instance=instructor_profile[0])
                messages.success(request, 'Profile Saved Successfully !')
            else:
                messages.warning(request, 'Some information is not valid !')

    return render(request, 'profile.html', context={'form': form})


@login_required
def view_profile(request):
    instructor = InstructorProfile.objects.filter(user=request.user)
    learner = LearnerProfile.objects.filter(user=request.user)
    dic = {}
    if instructor.exists():
        dic['instructor'] = instructor[0]
    elif learner.exists():
        dic['learner'] = learner[0]
    else:
        messages.warning(request, 'Profile does not exists !')

    return render(request, 'account/view_profile.html', context=dic)


@login_required
def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(request, 'account/password_change.html', context={'form': form})