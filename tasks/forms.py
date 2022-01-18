from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

class ToDoForm(forms.ModelForm):
    content= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model=ToDo
        fields='__all__'