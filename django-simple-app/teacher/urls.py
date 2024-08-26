from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [
    path("teachers/view", views.index, name="index"),
    path("teachers/<int:id>", views.view_teacher, name="view_teacher"),
    path("teachers/add/", views.add, name="add"),
    path("teachers/edit/<int:id>/", views.edit, name="edit"),
    path("teachersdelete/<int:id>/", views.delete, name="delete"),
]
