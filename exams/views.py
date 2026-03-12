from django.db.models import Avg
from django.shortcuts import render

from .models import Registration, Result, Student


def home(request):
	searched_email = request.GET.get("email", "").strip()
	student = None
	registrations = Registration.objects.none()
	results = Result.objects.none()
	average_grade = None

	if searched_email:
		student = Student.objects.filter(email__iexact=searched_email).first()
		if student:
			registrations = Registration.objects.select_related("exam").filter(
				student=student
			).order_by("exam__date")
			results = Result.objects.select_related("exam").filter(student=student).order_by(
				"exam__date"
			)
			average_grade = results.aggregate(avg=Avg("grade"))["avg"]

	return render(
		request,
		"exams/home.html",
		{
			"searched_email": searched_email,
			"student": student,
			"registrations": registrations,
			"results": results,
			"average_grade": average_grade,
		},
	)

