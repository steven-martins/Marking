from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Project

# Create your views here.


def index(request):
    list = Project.objects.all()
    context = {'list': list}
    return render(request, 'marks/index.html', context)


def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)

def results(request, project_id):
    response = "You're looking at the results of project %s."
    return HttpResponse(response % project_id)

def mark(request, project_id):
    return HttpResponse("You're mark on question %s." % project_id)