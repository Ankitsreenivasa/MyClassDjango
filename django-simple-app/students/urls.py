from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("", views.index, name="index"),
    path("students/<int:id>", views.view_student, name="view_student"),
    path("students/add/", views.add, name="add"),
    path("students/edit/<int:id>/", views.edit, name="edit"),
    path("students/delete/<int:id>/", views.delete, name="delete"),
]
