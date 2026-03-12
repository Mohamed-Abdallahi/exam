from django.test import TestCase
from django.urls import reverse

from .models import Exam, Registration, Result, Student


# Tests fonctionnels de la page d accueil etudiant.
class StudentRecordsViewTests(TestCase):
	def setUp(self):
		# Donnees de test: 1 etudiant, 2 examens, inscriptions et resultats.
		self.student = Student.objects.create(
			firstname="Ali",
			lastname="Hassan",
			email="ali@example.com",
		)
		self.math_exam = Exam.objects.create(title="Mathematics", date="2026-03-20")
		self.physics_exam = Exam.objects.create(title="Physics", date="2026-03-23")
		Registration.objects.create(student=self.student, exam=self.math_exam)
		Registration.objects.create(student=self.student, exam=self.physics_exam)
		Result.objects.create(student=self.student, exam=self.math_exam, grade=88.5)
		Result.objects.create(student=self.student, exam=self.physics_exam, grade=91.5)

	def test_home_page_displays_registrations_results_and_average(self):
		# Verifie le rendu des donnees et le calcul de la moyenne.
		response = self.client.get(
			reverse("home"),
			{"email": "ali@example.com"},
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Ali Hassan")
		self.assertContains(response, "Mathematics")
		self.assertContains(response, "Physics")
		self.assertContains(response, "90.00")

	def test_home_page_shows_not_found_message(self):
		# Verifie le message affiche quand l email n existe pas.
		response = self.client.get(
			reverse("home"),
			{"email": "missing@example.com"},
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Aucun etudiant trouve pour cette adresse email.")
