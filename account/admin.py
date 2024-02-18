from django.contrib import admin
from .models import User, InstructorProfile, LearnerProfile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_per_page = 10


@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_image', 'full_name', 'qualification',
                    'subject', 'phone_no', 'join_date')
    list_per_page = 10


@admin.register(LearnerProfile)
class LearnerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_image', 'full_name', 'study_in', 'insti_name',
                    'phone_no', 'date_of_birth', 'join_date')
    list_per_page = 10