from django import forms
from .models import Relation

class loginForm(forms.Form):
    name = forms.CharField(label='Your name:', max_length=15)