from django.shortcuts import render
from django.views.generic import TemplateView


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
