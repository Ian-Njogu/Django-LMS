from django.db import models
from courses.models import Course  
from django.conf import settings

# Model to represent a lecture within a course
class Lecture(models.Model):
    # Each lecture is linked to a course
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lectures'  # Allows access via course.lectures.all()
    )
    title = models.CharField(max_length=255)  # Title of the lecture
    content = models.TextField(blank=True)  # Optional lecture content/notes
    file = models.FileField(upload_to='lectures/', blank=True, null=True)  # Optional file upload
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.title})"  

# Model to represent an assignment for a course
class Assignment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='assignments'  
    )
    title = models.CharField(max_length=255)  # Title of the assignment
    description = models.TextField()  # Description/instructions for the assignment
    file = models.FileField(upload_to='assignments/', blank=True, null=True)  # Optional attached file 
    due_date = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.title} ({self.course.title})"  

# Model to represent a quiz under a course
class Quiz(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='quizzes'
    )
    title = models.CharField(max_length=255)  # Title of the quiz
    description = models.TextField(blank=True)  # Optional quiz instructions or notes
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.title} ({self.course.title})"

# Model for student assignment submissions
def upload_assignment_submission_path(instance, filename):
    return f"assignments/submissions/{instance.assignment.id}/{instance.student.id}/{filename}"

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignment_submissions')
    submitted_file = models.FileField(upload_to=upload_assignment_submission_path, blank=True, null=True)
    submitted_text = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ('assignment', 'student')

    def __str__(self):
        return f"{self.student.email} - {self.assignment.title}"

# Model for student quiz submissions
class QuizSubmission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='quiz_submissions')
    answers = models.TextField()  # For now, store as text- can be expanded for structured answers
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ('quiz', 'student')

    def __str__(self):
        return f"{self.student.email} - {self.quiz.title}"
