from django.urls import path
from .views import user_login, user_logout


urlpatterns = [
    path("user-login/", user_login, name="user_login"),
    path("user-logout/", user_logout, name="user_logout")
]
