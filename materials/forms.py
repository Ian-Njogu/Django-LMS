from django import forms
from .models import AssignmentSubmission, QuizSubmission

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['submitted_file', 'submitted_text']
        widgets = {
            'submitted_text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your assignment answer here...'}),
        }

class QuizSubmissionForm(forms.ModelForm):
    class Meta:
        model = QuizSubmission
        fields = ['answers']
        widgets = {
            'answers': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your quiz answers here...'}),
        } 