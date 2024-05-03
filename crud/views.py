from django.shortcuts import render, redirect
from .models import Student, ClassRoom


def student(request):
    students = Student.objects.all()
    return render(request, template_name="crud/student.html", context={"students": students})


def classroom(request):
    if request.method == "POST":
        print(request.POST)
        classroom_name = request.POST.get("classroom_name")
        ClassRoom.objects.create(name=classroom_name)
        return redirect("crud_classroom")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/classroom.html", context={"classrooms": classrooms})


def classroom_update(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        n = request.POST.get("classroom_name")
        c.name = n
        c.save()
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_update.html", context={"classroom": c})
