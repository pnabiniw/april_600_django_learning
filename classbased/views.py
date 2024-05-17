from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from crud.models import ClassRoom, Student, StudentProfile
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .forms import ClassRoomForm, ClassRoomModelForm, StudentModelForm


class HomeView(TemplateView):
    template_name = "classbased/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # dictionary
        context["name"] = "Hary"
        return context

    def get(self, *args, **kwargs):
        import json
        user = self.request.user
        with open("crud/counter.json", "r") as fp:
            data = fp.read()
            data = json.loads(data)
        data['crud_student_counter'] += 1
        with open("crud/counter.json", "w") as fp:
            data = json.dumps(data)
            fp.write(data)

        return super(HomeView, self).get(*args, **kwargs)


class ClassRoomView(ListView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom.html"
    context_object_name = "classrooms"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # form = ClassRoomForm()
        form = ClassRoomModelForm()
        context["form"] = form
        return context

    def post(self, *args, **kwargs):
        form = ClassRoomModelForm(self.request.POST)  # We are validating user input data
        if form.is_valid():
            print(form.cleaned_data)  # form.cleaned is a dict type
            # name = form.cleaned_data["name"]
            # ClassRoom.objects.create(name=name)
            form.save()
            messages.success(self.request, "Classroom added successfully !")
        else:
            messages.error(self.request, "Invalid Form data")
        return redirect("classbased:classroom")


class ClassroomListCreateView(CreateView):
    queryset = ClassRoom.objects.all()  # querysets are lazy in Django
    template_name = "classbased/classroom.html"
    form_class = ClassRoomModelForm
    success_url = reverse_lazy("classbased:classroom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = self.get_queryset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Classroom added successfully !")
            return self.form_valid(form)
        else:
            messages.error(request, "Something went wrong !")
            return self.form_invalid(form)


class ClassroomUpdateView(UpdateView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom_update.html"
    form_class = ClassRoomModelForm
    context_object_name = "classroom"
    success_url = reverse_lazy("classbased:classroom")


class ClassroomDeleteView(DeleteView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom_delete.html"
    success_url = reverse_lazy("classbased:classroom")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request, "Classroom deleted successfully !")
            return self.form_valid(form)  # deletes the classroom
        else:
            messages.error(self.request, "Something went wrong !")
            return self.form_invalid(form)


class StudentListView(ListView):
    queryset = Student.objects.all()
    template_name = "classbased/student.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "classbased/student_create.html"
    form_class = StudentModelForm
    success_url = reverse_lazy("classbased:student")
    next_form = ClassRoomModelForm

    def form_valid(self, form):
        self.object = form.save()
        student = self.object
        bio = form.cleaned_data['bio']
        phone = form.cleaned_data["phone_number"]
        StudentProfile.objects.create(student=student, bio=bio, phone=phone)
        messages.success(self.request, "Student added successfully !")
        return redirect("classbased:student")

    def form_invalid(self, form):
        messages.error(self.request, "Could not create student!")
        return super().form_invalid(form)


class StudentDetailView(DetailView):
    queryset = Student.objects.all()
    template_name = "classbased/student_detail.html"
    context_object_name = "student"


class StudentUpdateView(UpdateView):
    queryset = Student.objects.all()
    template_name = "classbased/student_update.html"
    form_class = StudentModelForm

    # success_url = reverse_lazy("classbased:student_detail")

    def get_success_url(self):
        return reverse_lazy("classbased:student_detail", self.get_object().id)

    def get_initial(self):
        student = self.get_object()
        initial = super().get_initial()
        try:
            profile = StudentProfile.objects.get(student=student)
        except:
            pass
        else:
            initial["bio"] = profile.bio
            initial["phone_number"] = profile.phone
            initial["profile_picture"] = profile.profile_picture
        return initial

    def form_valid(self, form):
        bio = form.cleaned_data.pop("bio")
        phone_number = form.cleaned_data.pop("phone_number")
        pp = form.cleaned_data.pop("profile_picture")
        student = form.save()
        # (<sp_object>, False)
        sp, _ = StudentProfile.objects.update_or_create(student=student,
                                                        defaults={"bio": bio, "phone": phone_number})
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("classbased:student_detail", student.id)


def student_detail_api_view(request, id):
    try:
        student = Student.objects.get(id=id)
    except:
        return JsonResponse({"detail": "Not Found"})
    response = {
        "name": student.name,
        "age": student.age,
        "email": student.email,
        "address": student.address
    }
    return JsonResponse(response)
