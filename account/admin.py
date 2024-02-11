from django.contrib import admin
from .models import User, InstructorProfile, LearnerProfile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Admin View for User'''

    list_display = ('id', 'email')
    list_per_page = 10


@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    '''Admin View for InstructorProfile'''

    list_display = ('id', 'full_name', 'qualification',
                    'subject', 'phone_no', 'profile_image', 'join_date')
    list_per_page = 10


@admin.register(LearnerProfile)
class LearnerProfileAdmin(admin.ModelAdmin):
    '''Admin View for LearnerProfile'''

    list_display = ('id', 'full_name', 'study_in', 'insti_name',
                    'phone_no', 'date_of_birth', 'join_date', 'profile_image')
    list_per_page = 10