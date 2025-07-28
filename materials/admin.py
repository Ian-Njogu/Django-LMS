from django.contrib import admin
from .models import Lecture, Assignment, Quiz, AssignmentSubmission, QuizSubmission

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

@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'submitted_at', 'grade')
    search_fields = ('assignment__title', 'student__email')
    list_filter = ('assignment', 'grade')

@admin.register(QuizSubmission)
class QuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'student', 'submitted_at', 'grade')
    search_fields = ('quiz__title', 'student__email')
    list_filter = ('quiz', 'grade')
