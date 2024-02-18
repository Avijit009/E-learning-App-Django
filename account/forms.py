from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, InstructorProfile, LearnerProfile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'is_instructor']


class InstructorProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = InstructorProfile
        fields = ['profile_image', 'full_name', 'qualification', 'subject', 'date_of_birth', 'phone_no']


class LearnerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = LearnerProfile
        fields = ['profile_image', 'full_name', 'study_in',
                  'insti_name', 'phone_no', 'date_of_birth']