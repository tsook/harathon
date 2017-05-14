from django import forms
from .models import Relation, Member

class memberForm(forms.ModelForm):
	class Meta:
		model = Member
		fields = ('username', 'group_id')

class moneyForm(forms.ModelForm):
	class Meta:
		model = Relation
		fields = ('giver', 'receiver', 'money', 'text',)
'''
class profileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('username', 'passwrd')
'''