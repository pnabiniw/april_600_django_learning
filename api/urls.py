from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("student/", views.StudentView.as_view(), name="student"),
    path("student/<int:id>/", views.StudentDetailView.as_view(), name="student_detail"),
    path("classroom/", views.ClassRoomView.as_view(), name="classroom"),
    path("classroom/<int:id>/", views.ClassRoomView.as_view(), name="classroom_patch"),
]


using_serializer_paths = [
    path('classroom-using-serializer/<int:id>/', views.ClassRoomUsingSerializerDetailView.as_view()),
    path("using-serializer/classroom/", views.ClassRoomUsingSerializerView.as_view()),
    path("using-serializer/student/", views.StudentUsingSerializerView.as_view()),
]

using_model_serializer_paths = [
    path("using-model-serializer/student/", views.StudentUsingModelSerView.as_view())
]

urlpatterns += using_serializer_paths + using_model_serializer_paths
