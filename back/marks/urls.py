__author__ = 'Steven'


from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<project_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<project_id>[0-9]+)/editsec/$', views.editsec, name='editsec'),
    # ex: /polls/5/mark/
    url(r'^(?P<project_id>[0-9]+)/mark/$', views.mark, name='grade'),
]

