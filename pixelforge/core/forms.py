from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'status', 'project_lead']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'project_lead': forms.Select(attrs={'class': 'form-select'}),
        }

#assign developers to project

from .models import User

class AssignDeveloperForm(forms.Form):
    developers = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(role='dev'),
        widget=forms.CheckboxSelectMultiple
    )
#document upload form
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']


#login form
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ))