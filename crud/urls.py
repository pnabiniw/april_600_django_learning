from django.urls import path
from .views import student, classroom, classroom_update, classroom_delete, add_student

urlpatterns = [
    path("classroom/<int:id>/", classroom_update, name="crud_classroom_update"),
    path("classroom-delete/<int:id>/", classroom_delete, name="crud_classroom_delete"),
    path('classroom/', classroom, name="crud_classroom"),
    path('add-student/', add_student, name="crud_add_student"),
    path('', student, name="crud_student"),
]
