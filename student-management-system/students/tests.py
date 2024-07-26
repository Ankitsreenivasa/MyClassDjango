import random
from django.test import TestCase
from .models import Student


class StudentModelUnitTestCase(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            usn=random.randint(10000, 99999),
            full_name='Bob',
            tyl_eligibility='Smith',
            email='bob.smith@test.com',
            department='Computer Science',
            cgpa=3.92
        )

    def test_student_model(self):
        data = self.student
        self.assertIsInstance(data, Student)
