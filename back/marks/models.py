from django.db import models
from datetime import datetime

class Student(models.Model):
    login = models.CharField(max_length=10, primary_key=True)
    last_connection = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.login


class Picture(models.Model):
    #data = models.BinaryField()
    file = models.ImageField(upload_to="picture/%Y/%m/%d", max_length=150)
    title = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s " % (self.title, str(self.file))

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Student)
    #picture_cover = models.ForeignKey(Picture, null=True)
    pictures = models.ManyToManyField(Picture, blank=True)

    marks = models.ManyToManyField(Student, through='Mark', related_name="project_marks_student")

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

class Mark(models.Model):
    student = models.ForeignKey(Student)
    project = models.ForeignKey(Project)
    question = models.ForeignKey(Question)
    result = models.IntegerField()

    def __str__(self):
        return "Mark(%s) by %s for %s" % (self.result, self.student, self.question)
