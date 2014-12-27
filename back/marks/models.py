from django.db import models
from datetime import datetime

class Student(models.Model):
    login = models.CharField(max_length=10, primary_key=True)
    last_connection = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.login


class Picture(models.Model):
    #data = models.BinaryField()
    file = models.ImageField(upload_to="picture/%Y/%m/%d")
    title = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s " % (self.title, str(self.file))

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(Student)
    #picture_cover = models.ForeignKey(Picture, null=True)
    pictures = models.ManyToManyField(Picture)