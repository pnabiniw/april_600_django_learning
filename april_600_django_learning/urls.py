from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("commons/", include("commons.urls")),
    path('crud/', include('crud.urls')),
    path("", include("myapp.urls"))  # URL Chaining
]
