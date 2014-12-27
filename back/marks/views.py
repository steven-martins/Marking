from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the marks index.")


def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def results(request, project_id):
    response = "You're looking at the results of project %s."
    return HttpResponse(response % project_id)

def mark(request, project_id):
    return HttpResponse("You're mark on question %s." % project_id)