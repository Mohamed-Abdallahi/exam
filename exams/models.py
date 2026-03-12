from django.db import models


# Modele representant un etudiant.
class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


    # Modele representant un examen.
class Exam(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title


# Inscription d un etudiant a un examen.
class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


# Resultat (note) d un etudiant pour un examen.
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    grade = models.FloatField()