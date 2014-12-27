from django.contrib import admin

from .models import Project, Picture, Student

# Register your models here.
admin.site.register(Project)
admin.site.register(Picture)
admin.site.register(Student)