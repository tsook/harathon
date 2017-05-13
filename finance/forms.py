from django import forms

class loginForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=15)