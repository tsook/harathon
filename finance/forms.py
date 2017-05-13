from django import forms
from .models import Relation

class loginForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=15)

class moneyForm(forms.ModelForm):
	class Meta:
		model = Relation
		fields = ('giver', 'receiver', 'money', 'text',)
	

