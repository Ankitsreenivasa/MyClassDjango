from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['usn', 'full_name', 'tyl_eligibility', 'email', 'department', 'cgpa']
    labels = {
      'usn': 'USN',
      'full_name': 'Full Name',
      'tyl_eligibility': 'TYL Eligibility',
      'email': 'Email',
      'department': 'Department',
      'cgpa': 'Ccgpa'
    }
    widgets = {
      'usn': forms.TextInput(attrs={'class': 'form-control'}),
      'full_name': forms.TextInput(attrs={'class': 'form-control'}),
      'tyl_eligibility': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'department': forms.TextInput(attrs={'class': 'form-control'}),
      'cgpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }
