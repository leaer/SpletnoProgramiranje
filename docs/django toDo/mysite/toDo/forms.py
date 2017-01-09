from django.contrib.auth.models import User
from django import forms
from .models import Uporabnik, Opravilo

class UserForm(forms.ModelForm):
	geslo = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Uporabnik
		fields = ['ime', 'priimek', 'email', 'uporabniskoIme', 'geslo']


class OpraviloForm(forms.ModelForm):
	class Meta:
		model = Opravilo
		fields =  ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski']
