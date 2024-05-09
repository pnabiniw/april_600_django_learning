from django.shortcuts import render
from django.http import HttpResponse


def quiz_home(request):
    return HttpResponse("Quiz Home")
