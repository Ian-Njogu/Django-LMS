from django.contrib import admin
from .models import Lecture, Assignment, Quiz

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'upload_date')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'due_date', 'created_at')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'created_at')
    search_fields = ('title', 'course__title')
    list_filter = ('course',)
