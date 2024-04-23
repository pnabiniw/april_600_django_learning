from django.urls import path
from .views import home, home_detail, portfolio

urlpatterns = [
    path("home/<int:id>/detail/", home_detail),
    path("portfolio/", portfolio),
    path("", home),
]
