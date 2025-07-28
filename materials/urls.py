from django.urls import path
from . import views

urlpatterns = [
    path('assignment/<int:assignment_id>/submit/', views.assignment_submit, name='assignment_submit'),
    path('assignment/<int:assignment_id>/feedback/', views.assignment_feedback, name='assignment_feedback'),
    path('quiz/<int:quiz_id>/submit/', views.quiz_submit, name='quiz_submit'),
    path('quiz/<int:quiz_id>/feedback/', views.quiz_feedback, name='quiz_feedback'),
] 