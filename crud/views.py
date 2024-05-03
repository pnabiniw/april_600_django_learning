from django.shortcuts import render, redirect
from .models import Student, ClassRoom


def student(request):
    students = Student.objects.all().order_by('-id')
    return render(request, template_name="crud/student.html", context={"students": students})


def classroom(request):
    if request.method == "POST":
        print(request.POST)
        classroom_name = request.POST.get("classroom_name")
        ClassRoom.objects.create(name=classroom_name)
        return redirect("crud_classroom")
    classrooms = ClassRoom.objects.all().order_by('-id')
    return render(request, template_name="crud/classroom.html", context={"classrooms": classrooms})


def classroom_update(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        n = request.POST.get("classroom_name")
        c.name = n
        c.save()
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_update.html", context={"classroom": c})


def classroom_delete(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        c.delete()
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_delete.html", context={"classroom": c})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        if classroom_id != "null":
            Student.objects.create(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        else:
            Student.objects.create(name=name, age=age, email=email, address=address)
        return redirect("crud_student")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/add_student.html", context={"classrooms": classrooms})
