from django.db import models


# Create your models here.
class Student(models.Model):
  usn = models.CharField(max_length=20, null=True, blank=True)
  full_name = models.CharField(max_length=50)
  tyl_eligibility = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  department = models.CharField(max_length=50)
  cgpa = models.FloatField()

  def __str__(self):
    return f'Student: {self.full_name}'
