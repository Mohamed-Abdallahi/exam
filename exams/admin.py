from django.contrib import admin
from .models import Student, Exam, Registration, Result

# Enregistrement des modeles dans l interface d administration.
admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Registration)
admin.site.register(Result)