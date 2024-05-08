from django.shortcuts import render, redirect
from .models import Student, ClassRoom, StudentProfile


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
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        if classroom_id != "null":
            s = Student.objects.create(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        else:
            s = Student.objects.create(name=name, age=age, email=email, address=address)
        StudentProfile.objects.create(phone=phone, bio=bio, student=s)
        return redirect("crud_student")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/add_student.html", context={"classrooms": classrooms})


def detail_student(request, id):
    s = Student.objects.get(id=id)
    return render(request, template_name="crud/detail_student.html", context={"student": s})


def delete_student(request, id):
    s = Student.objects.get(id=id)
    if request.method == "POST":
        s.delete()
        return redirect("crud_student")
    return render(request, template_name="crud/delete_student.html", context={"student": s})


def update_student(request, id):
    print(id)
    s = Student.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        pp = request.FILES.get("profile_picture")  # None
        pp_clear = request.POST.get("pp_clear")
        Student.objects.filter(id=id).update(name=name, age=age, email=email, address=address,
                                             classroom_id=classroom_id)
        sp, created = StudentProfile.objects.update_or_create(student=s, defaults={"phone": phone, "bio": bio})

        if pp:
            extension = pp.name.split(".")[-1]   # nfdkjhfds.png => ["nfdkjhfds", "png"]
            if extension not in ["jpg", "jpeg", "png", "PNG", "JPG"]:
                return redirect("update_student", id)
            sp.profile_picture = pp
        if pp_clear == "on":
            sp.profile_picture = None
        sp.save()
        return redirect("detail_student", id)
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/update_student.html", context={"student": s,
                                                                              "classrooms": classrooms})
