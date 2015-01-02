__author__ = 'Steven'

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


def index(request):
    return HttpResponseRedirect(reverse('marks:index'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('marks:index'))

