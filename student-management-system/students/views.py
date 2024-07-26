from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm


# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_usn = form.cleaned_data['usn']
      new_full_name = form.cleaned_data['full_name']
      new_tyl_eligibility = form.cleaned_data['tyl_eligibility']
      new_email = form.cleaned_data['email']
      new_department = form.cleaned_data['department']
      new_cgpa = form.cleaned_data['cgpa']

      new_student = Student(
        usn=new_usn,
        full_name=new_full_name,
        tyl_eligibility=new_tyl_eligibility,
        email=new_email,
        department=new_department,
        cgpa=new_cgpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))
