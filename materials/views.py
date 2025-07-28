from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Assignment, AssignmentSubmission, Quiz, QuizSubmission
from .forms import AssignmentSubmissionForm, QuizSubmissionForm

# Create your views here.

@login_required
def assignment_submit(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    student = request.user
    # Only allow students
    if student.role != 'student':
        return HttpResponseForbidden()
    # Only one submission per student per assignment
    submission, created = AssignmentSubmission.objects.get_or_create(assignment=assignment, student=student)
    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('assignment_feedback', assignment_id=assignment.id)
    else:
        form = AssignmentSubmissionForm(instance=submission)
    return render(request, 'materials/assignment_submit.html', {'form': form, 'assignment': assignment, 'submission': submission})

@login_required
def assignment_feedback(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    student = request.user
    submission = AssignmentSubmission.objects.filter(assignment=assignment, student=student).first()
    return render(request, 'materials/assignment_feedback.html', {'assignment': assignment, 'submission': submission})

@login_required
def quiz_submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    student = request.user
    if student.role != 'student':
        return HttpResponseForbidden()
    submission, created = QuizSubmission.objects.get_or_create(quiz=quiz, student=student)
    if request.method == 'POST':
        form = QuizSubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('quiz_feedback', quiz_id=quiz.id)
    else:
        form = QuizSubmissionForm(instance=submission)
    return render(request, 'materials/quiz_submit.html', {'form': form, 'quiz': quiz, 'submission': submission})

@login_required
def quiz_feedback(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    student = request.user
    submission = QuizSubmission.objects.filter(quiz=quiz, student=student).first()
    return render(request, 'materials/quiz_feedback.html', {'quiz': quiz, 'submission': submission})
