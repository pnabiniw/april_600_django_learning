from django.shortcuts import render
from .models import Student


def student(request):
    students = Student.objects.all()
    return render(request, template_name="crud/student.html", context={"students": students})
