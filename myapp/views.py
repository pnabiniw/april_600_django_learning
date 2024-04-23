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
