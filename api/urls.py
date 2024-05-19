from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("student/", views.StudentView.as_view(), name="student"),
    path("student/<int:id>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("classroom/", views.ClassRoomView.as_view(), name="classroom")
]
