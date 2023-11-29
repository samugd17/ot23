from django.contrib import admin

from .models import Competitor, Judge, MusicStyle, Teacher


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'slug',
        'birthdate',
        'city',
        'hobbies',
        'style',
        'avatar',
    ]
    list_filter = ['first_name', 'last_name', 'style']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug', 'subject', 'avatar']
    list_filter = ['first_name', 'last_name', 'subject']


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug', 'job', 'avatar']
    list_filter = ['first_name', 'last_name']


@admin.register(MusicStyle)
class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
