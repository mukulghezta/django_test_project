from django import forms
from django.db.models import fields
from . import models

class CreatePerson(forms.ModelForm):
    class Meta:
        model   = models.Person
        fields  = ['username', 'phone', 'pic']