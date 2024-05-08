from django.shortcuts import render
from crud.models import Student


def student(request):
    # students = [
    #     {"name": "Jon", "age": 30, "email": "jon@email.com", "address": "KTM"},
    #     {"name": "Ram", "age": 20, "email": "jon@email.com", "address": "KTM"},
    #     {"name": "Jane", "age": 25, "email": "jon@email.com", "address": "KTM"},
    #     {"name": "Hary", "age": 27, "email": "jon@email.com", "address": "KTM"},
    # ]
    students = Student.objects.all()
    print(students[0])
    return render(request, template_name="commons/student.html", context={"students": students})


def classroom(request):
    classrooms = [
        {"name": "One", "section": "A"},
        {"name": "Two", "section": "B"},
        {"name": "Three", "section": "B"},
        {"name": "Four", "section": "A"},
        {"name": "Five", "section": "B"},
    ]
    return render(request, "commons/classroom.html", {"classrooms": classrooms})


def not_found_404(r, *args, **kwargs):
    return render(r, template_name='404_not_found.html')
