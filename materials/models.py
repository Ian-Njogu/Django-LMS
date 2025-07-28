from django.db import models
from courses.models import Course  

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
