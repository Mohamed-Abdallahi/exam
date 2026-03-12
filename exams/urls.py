from django.urls import path

from . import views

# Routes de l application exams.
urlpatterns = [
    # Page d accueil du portail etudiant.
    path("", views.home, name="home"),
]
