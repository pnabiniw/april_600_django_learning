from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("commons/", include("commons.urls")),
    path('crud/', include('crud.urls')),
    path("", include("myapp.urls"))  # URL Chaining
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
