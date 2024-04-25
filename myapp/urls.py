from django.urls import path
from .views import home, home_detail, portfolio, test, root_page, learning_context, using_bootstrap

urlpatterns = [
    path("home/<int:id>/detail/", home_detail, name="home_detail"),
    path("test/", test, name="test"),
    path("portfolio/", portfolio, name="portfolio"),
    path("learning-context/", learning_context, name="learning_context"),
    path("using-bootstrap/", using_bootstrap, name="u_boots"),
    path("", root_page, name="root_page"),
    path("", home),
]
