from django.shortcuts import render, redirect
from crud.models import ClassRoom
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .forms import ClassRoomForm


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
        form = ClassRoomForm()
        context["form"] = form
        return context

    def post(self, *args, **kwargs):
        form = ClassRoomForm(self.request.POST)  # We are validating user input data
        if form.is_valid():
            print(form.cleaned_data)  # form.cleaned is a dict type
            name = form.cleaned_data["name"]
            ClassRoom.objects.create(name=name)
            messages.success(self.request, "Classroom added successfully !")
        else:
            messages.error(self.request, "Invalid Form data")
        return redirect("classbased:classroom")
