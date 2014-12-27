from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from .models import Project, Question, Mark, Student

# Create your views here.


def index(request):
    list = Project.objects.all()
    context = {'list': list}
    return render(request, 'marks/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    questions = get_list_or_404(Question)
    context = {'project': project, 'questions': questions}
    return render(request, 'marks/project.html', context)

def results(request, project_id):

    return HttpResponse("Results for %s. You are: %s" % (project_id, request.user))

def mark(request, project_id):
    #grade
    p = get_object_or_404(Project, pk=project_id)
    stud = Student.objects.get(login="mart_s")

    for key, value in request.POST.items():
        if key.startswith("question-"):
            try:
                quest = Question.objects.get(pk=int(key[9:]))
                mark = Mark.objects.get(student=stud, project=p, question=quest)
                #selected_choice = p.choice_set.get(pk=request.POST['choice'])
            #except Question.DoesNotExist:
            #    pass
            except Mark.DoesNotExist:
                mark = Mark(student=stud, project=p, question=quest)
                # Redisplay the question voting form.
                #return render(request, 'polls/detail.html', {
                #    'question': p,
                #    'error_message': "You didn't select a choice.",
                #})
            finally:
                mark.result = int(value)
                mark.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('marks:results', args=(p.id,)))

