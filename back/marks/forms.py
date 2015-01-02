
__author__ = 'Steven'


from django import forms

#class UploadFileForm(forms.Form):
#    title = forms.CharField(max_length=50)
#    file = forms.FileField()

from django.forms import ModelForm

from .models import Picture, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class PictureForm(ModelForm):
     class Meta:
         model = Picture
