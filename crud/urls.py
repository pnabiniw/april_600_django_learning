from django.urls import path
from .views import student, classroom, classroom_update, classroom_delete, add_student, detail_student, \
    delete_student

urlpatterns = [
    path("classroom/<int:id>/", classroom_update, name="crud_classroom_update"),
    path("classroom-delete/<int:id>/", classroom_delete, name="crud_classroom_delete"),
    path('classroom/', classroom, name="crud_classroom"),
    path('add-student/', add_student, name="crud_add_student"),
    path("detail-student/<int:id>/", detail_student, name="detail_student"),
    path("delete-student/<int:id>/", delete_student, name="delete_student"),
    path('', student, name="crud_student"),
]
