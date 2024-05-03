from django.urls import path
from .views import student, classroom, classroom_update

urlpatterns = [
    path("classroom/<int:id>/", classroom_update, name="crud_classroom_update"),
    path('classroom/', classroom, name="crud_classroom"),
    path('', student, name="crud_student"),
]
