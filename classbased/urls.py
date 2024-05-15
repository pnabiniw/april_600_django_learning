from django.urls import path
from . import views

app_name = "classbased"

urlpatterns = [
    # path("classroom/", views.ClassRoomView.as_view(), name="classroom"),
    path("classroom/", views.ClassroomListCreateView.as_view(), name="classroom"),
    path("classroom-update/<int:pk>/", views.ClassroomUpdateView.as_view(), name="classroom_update"),
    path("classroom-delete/<int:pk>/", views.ClassroomDeleteView.as_view(), name="classroom_delete"),
    path("", views.HomeView.as_view(), name="home"),
]
