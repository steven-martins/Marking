from django.contrib import admin

from .models import Project, Picture, Mark, Question, Timeslot

# Register your models here.
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(Mark)
admin.site.register(Question)
admin.site.register(Timeslot)