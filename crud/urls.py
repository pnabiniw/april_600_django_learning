from django.urls import path
from .views import student


urlpatterns = [
    path('', student, name="crud_student"),
]
