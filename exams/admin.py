from django.contrib import admin
from .models import Student, Exam, Registration, Result

admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Registration)
admin.site.register(Result)