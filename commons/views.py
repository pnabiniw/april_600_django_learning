from django.shortcuts import render


def student(request):
    return render(request, template_name="commons/student.html")
