from django.db import models
from django.conf import settings  # Import the settings module to access AUTH_USER_MODEL

# Course model to represent a course in the system
class Course(models.Model):
    title = models.CharField(max_length=255)  # Title of the course
    description = models.TextField()  # Detailed description of the course
    
    # Prerequisites for the course - can be multiple and are optional
    # This allows a course to have prerequisites that are also courses
    # symmetrical=False allows A to be a prerequisite for B without B being one for A
    prerequisites = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='required_for'
    )

    # Instructors teaching this course - only users with the role 'instructor'
    instructors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'instructor'},
        related_name='courses_taught'
    )

    # Optional field to specify course timing or schedule
    schedule = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title  

# Enrollment model to track student-course relationships
class Enrollment(models.Model):
    # Define the possible enrollment statuses
    STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]

    # Student who is enrolled - must be a user with role 'student'
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='enrollments'
    )

    # The course the student is enrolled in
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    # Date and time of enrollment 
    enrollment_date = models.DateTimeField(auto_now_add=True)

    # Status of the enrollment
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='enrolled'
    )

    class Meta:
        # Prevent duplicate enrollments for the same student in the same course
        unique_together = ('student', 'course')

    def __str__(self):
       
        return f"{self.student.email} - {self.course.title}"
