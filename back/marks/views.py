from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


from .models import Project, Question, Mark, Picture
from .forms import PictureForm, ProjectForm
from django.core.exceptions import PermissionDenied

#@login_required
def index(request):
    list = []
    if request.user.is_authenticated():
        list = Project.objects.all() # shared timeslot only
    context = {'list': list}
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
    for q in questions_raw:
        value = None
        for m in marks:
            if q.pk == m.question.pk:
                value = m.result
        questions.append((q, value))

    shared_timeslot = False
    for proj in Project.objects.filter(members=request.user):
        if not shared_timeslot and project.timeslot == proj.timeslot:
            shared_timeslot = True
    context = {'project': project, 'questions': questions, "shared_timeslot": shared_timeslot}
    return render(request, 'marks/project.html', context)


@login_required
def editsec(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user not in project.members.all():
        raise PermissionDenied
    if request.method == 'POST':

        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            proj = form.save()
            #instance = Picture(file=request.FILES['file'])
            #instance.set_title(form.title)
            #instance.save()
            proj.save()
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
    return render(request, 'marks/edit.html', {'form': form, 'project':project})

@login_required
def mark(request, project_id):
     # TODO: shared timeslot only
    p = get_object_or_404(Project, pk=project_id)
    if request.user in p.members.all():
        raise PermissionDenied
    for key, value in request.POST.items():
        if key.startswith("question-"):
            try:
                quest = Question.objects.get(pk=int(key[9:]))
                ma = Mark.objects.get(student=request.user, project=p, question=quest)
                #selected_choice = p.choice_set.get(pk=request.POST['choice'])
            #except Question.DoesNotExist:
            #    pass
            except Mark.DoesNotExist:
                ma = Mark(student=request.user, project=p, question=quest)
            finally:
                ma.result = int(value)
                ma.save()
    return HttpResponseRedirect(reverse('marks:detail', args=(p.id,)))
