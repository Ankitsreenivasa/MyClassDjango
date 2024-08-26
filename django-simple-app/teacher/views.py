from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Teacher
from .forms import TeacherForm


def index(request):
    return render(request, "teachers/index.html", {"teachers": Teacher.objects.all()})


def view_teacher(request, id):
    return HttpResponseRedirect(reverse("index"))


def add(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            new_teacher = form.save()
            return render(
                request, "teachers/add.html", {"form": TeacherForm(), "success": True}
            )
    else:
        form = TeacherForm()
    return render(request, "teachers/add.html", {"form": TeacherForm()})


def edit(request, id):
    if request.method == "POST":
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return render(
                request, "teachers/edit.html", {"form": form, "success": True}
            )
    else:
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(instance=teacher)
    return render(request, "teachers/edit.html", {"form": form})


def delete(request, id):
    if request.method == "POST":
        teacher = Teacher.objects.get(pk=id)
        teacher.delete()
    return HttpResponseRedirect(reverse("teachers:index"))
