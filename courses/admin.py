from django.contrib import admin
from .models import Course, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    filter_horizontal = ('prerequisites', 'instructors')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'status')
    list_filter = ('status', 'course')
    search_fields = ('student__email', 'course__title')
