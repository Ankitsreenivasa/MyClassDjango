from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "teacher_id",
            "first_name",
            "last_name",
            "email",
            "department",
            "hire_date",
        ]
        labels = {
            "teacher_id": "Teacher ID",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email",
            "department": "Department",
            "hire_date": "Hire Date",
        }
        widgets = {
            "teacher_id": forms.NumberInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "department": forms.TextInput(attrs={"class": "form-control"}),
            "hire_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }
