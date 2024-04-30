from django.urls import path
from .views import student, classroom


urlpatterns = [
    path('', student, name="crud_student"),
    path('classroom/', classroom, name="crud_classroom")
]
