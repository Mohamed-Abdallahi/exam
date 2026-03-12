from django.contrib import admin
from django.urls import include, path

# Routes principales du projet.
urlpatterns = [
    # Interface d administration Django.
    path('admin/', admin.site.urls),
    # Routes de l application metier exams.
    path('', include('exams.urls')),
]
