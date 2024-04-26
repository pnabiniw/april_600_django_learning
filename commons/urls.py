from django.urls import path
from .views import student, classroom


urlpatterns = [
    path("classroom/", classroom, name="commons_classroom"),
    path("", student, name="commons_student")
]
