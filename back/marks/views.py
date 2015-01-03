from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


from .models import Project, Question, Mark, Picture
from .forms import PictureForm, ProjectForm
from django.core.exceptions import PermissionDenied

@login_required
def index(request):
    l = []
    all_list = Project.objects.all() # shared timeslot only
    timeslots = list(set([proj.timeslot for proj in Project.objects.filter(members=request.user)]))
    for proj in all_list:
        if proj.timeslot in timeslots:
            l.append(proj)
    projects_rated = list(set([m.project for m in Mark.objects.filter(student=request.user)]))
    context = {'list': l, 'projects_rated': projects_rated}
    return render(request, 'marks/index.html', context)

@login_required
def myprojects(request):
    my_projects = []
    if request.user.is_authenticated():
        my_projects = Project.objects.filter(members=request.user)

    context = {'my_projects': my_projects}
    return render(request, 'marks/myprojects.html', context)


@login_required
def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    questions_raw = Question.objects.all()
    marks = Mark.objects.filter(student=request.user, project=project)
    questions = []
    entirely_marked = True
    for q in questions_raw:
        value = None
        for m in marks:
            if q.pk == m.question.pk:
                value = m.result
        if entirely_marked and not value:
            entirely_marked = False
        questions.append((q, value))
    shared_timeslot = False
    for proj in Project.objects.filter(members=request.user):
        if not shared_timeslot and project.timeslot == proj.timeslot:
            shared_timeslot = True
    context = {'project': project, 'questions': questions, "shared_timeslot": shared_timeslot,
               'entirely_marked': entirely_marked}
    return render(request, 'marks/project.html', context)

@login_required
def deleteimg(request, project_id, pict_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user not in project.members.all():
        raise PermissionDenied
    pict = get_object_or_404(Picture, pk=pict_id)
    pict.delete()
    return HttpResponseRedirect(reverse('marks:detail', args=(project.id,)))


@login_required
def editsec(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user not in project.members.all():
        raise PermissionDenied
    if request.method == 'POST':

        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            proj = form.save()
            #proj.save()
            return HttpResponseRedirect(reverse('marks:detail', args=(project.id,)))
    else:
        form = ProjectForm(instance=project)
    return render(request, 'marks/project.html', {'form': form, 'project':project})


@login_required
def edit(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user not in project.members.all():
        raise PermissionDenied
    if request.method == 'POST':

        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            pict = form.save()
            project.pictures.add(pict)
            #instance = Picture(file=request.FILES['file'])
            #instance.set_title(form.title)
            #instance.save()
            return HttpResponseRedirect(reverse('marks:detail', args=(project.id,)))
    else:
        form = PictureForm()
    return render(request, 'marks/project.html', {'form_pict': form, 'project':project})

@login_required
def mark(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    if request.user in p.members.all():
        raise PermissionDenied
    shared_timeslot = False
    for proj in Project.objects.filter(members=request.user):
        if not shared_timeslot and p.timeslot == proj.timeslot:
            shared_timeslot = True
    if not shared_timeslot:
        raise PermissionDenied
    for key, value in request.POST.items():
        if key.startswith("question-"):
            try:
                quest = Question.objects.get(pk=int(key[9:]))
                ma = Mark.objects.get(student=request.user, project=p, question=quest)
            except Mark.DoesNotExist:
                ma = Mark(student=request.user, project=p, question=quest)
            finally:
                ma.result = int(value)
                ma.save()
    return HttpResponseRedirect(reverse('marks:detail', args=(p.id,)))
