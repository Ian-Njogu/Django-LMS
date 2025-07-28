from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Custom manager to handle user creation logic
class UserManager(BaseUserManager):
    # Method to create a regular user
    def create_user(self, email, password=None, role='student', **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')  # Ensure email is provided
        email = self.normalize_email(email)  # Normalize the email (e.g., lowercasing domain part)
        user = self.model(email=email, role=role, **extra_fields)  # Create user instance
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save to the database using the default DB
        return user

    # Method to create a superuser (admin)
    def create_superuser(self, email, password=None, **extra_fields):
        # Ensure required flags are set for superuser
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, role='admin', **extra_fields)  # Use create_user method

# Custom user model inheriting from Django's base user classes
class User(AbstractBaseUser, PermissionsMixin):
    # Role options for the user
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    ]

    email = models.EmailField(unique=True)  # Email as the unique identifier
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')  # User role with default as student
    is_active = models.BooleanField(default=True)  # Indicates if the user account is active
    is_staff = models.BooleanField(default=False)  # Determines access to the admin site
    date_joined = models.DateTimeField(auto_now_add=True)  # Timestamp when user joined

    USERNAME_FIELD = 'email'  # Field used for login (instead of default username)
    REQUIRED_FIELDS = []  # No additional fields are required when creating superuser via CLI

    objects = UserManager()  # Link the custom user manager

    def __str__(self):
        return self.email  # Display email when user instance is printed
