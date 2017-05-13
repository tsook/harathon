from django import forms
from .models import Relation

class loginForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=15)

class moneyForm(forms.ModelForm):
	'''
	giver = forms.CharField(label='Owed by', max_length=50)
	receiver = forms.CharField(label='Owed to', max_length=50)
	money = forms.IntegerField(label='Amount')
	text = forms.CharField(label="For?", max_length=100)
	'''
	class Meta:
		model = Relation
		fields = ('giver', 'receiver', 'money', 'text',)
	

