from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # here request is the Django WSGIRequest Object
    query_strings = request.GET
    name = query_strings.get("name")
    print(name)
    print(request.scheme)
    print(request.method)
    print(request.user)
    print(request.get_full_path())
    return HttpResponse(f"<h1>Hello World. I am {name}</h1>")


def home_detail(request, id):
    return HttpResponse(f"<h1>My home id is {id}")


def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")


def test(request):
    return render(request, template_name="myapp/test.html")


def root_page(request):
    return render(request, template_name="myapp/root_page.html")


def learning_context(request):
    student = {"name": "Jon", "age": 30, "email": "jon@email.com", "address": "KTM"}
    students = [
        {"name": "Jon", "age": 30, "email": "jon@email.com", "address": "KTM"},
        {"name": "Ram", "age": 20, "email": "jon@email.com", "address": "KTM"},
        {"name": "Jane", "age": 25, "email": "jon@email.com", "address": "KTM"},
        {"name": "Hary", "age": 27, "email": "jon@email.com", "address": "KTM"},
    ]
    return render(request, "myapp/learning_context.html", context={"students": students, "student": student})


def using_bootstrap(request):
    students = [
        {"name": "Jon", "age": 30, "email": "jon@email.com", "address": "KTM"},
        {"name": "Ram", "age": 20, "email": "jon@email.com", "address": "KTM"},
        {"name": "Jane", "age": 25, "email": "jon@email.com", "address": "KTM"},
        {"name": "Hary", "age": 27, "email": "jon@email.com", "address": "KTM"},
    ]
    return render(request, template_name="myapp/using_bs.html", context={"students": students})
