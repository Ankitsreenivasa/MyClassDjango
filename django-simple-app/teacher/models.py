from django.db import models


class Teacher(models.Model):
    teacher_id = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=50)
    hire_date = models.DateField()

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"
