from django.urls import path
from . import views

app_name = "classbased"

urlpatterns = [
    path("classroom/", views.ClassRoomView.as_view(), name="classroom"),
    path("", views.HomeView.as_view(), name="home")
]
