from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    #data = models.BinaryField()
    file = models.ImageField(upload_to="picture/%Y/%m/%d", max_length=150)
    title = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s " % (self.title, str(self.file))

class Timeslot(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User)
    #picture_cover = models.ForeignKey(Picture, null=True)
    pictures = models.ManyToManyField(Picture, blank=True)
    timeslot = models.ForeignKey(Timeslot, blank=True)
    marks = models.ManyToManyField(User, through='Mark', related_name="project_marks_student")

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title

class Mark(models.Model):
    student = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    question = models.ForeignKey(Question)
    result = models.IntegerField()

    def __str__(self):
        return "Mark(%s) by %s for %s" % (self.result, self.student, self.question)
