
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index_url"),
    path("studentlist/", views.students, name="studentlist_url"),
]
