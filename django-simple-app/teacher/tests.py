import random
from django.test import TestCase
from .models import Teacher
from django.utils import timezone


class TeacherModelUnitTestCase(TestCase):
    def setUp(self):
        self.teacher = Teacher.objects.create(
            teacher_id=random.randint(1000, 9999),
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@test.com",
            department="Mathematics",
            hire_date=timezone.now().date(),
        )

    def test_teacher_model(self):
        data = self.teacher
        self.assertIsInstance(data, Teacher)


# Create your tests here.
