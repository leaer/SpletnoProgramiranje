from django.contrib.auth.models import User
from django import forms
from .models import Uporabnik, Opravilo
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.Form):
	username=forms.CharField(max_length=20)
	first_name=forms.CharField(max_length=20)
	last_name=forms.CharField(max_length=20)
	email=forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']


class OpraviloForm(forms.ModelForm):
	class Meta:
		model = Opravilo
		fields =  ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski']


class LoginForm(forms.Form):
	username=forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'password']

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UrediOpraviloForm(forms.ModelForm):
	class Meta:
		model = Opravilo
		fields = ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski', 'opravljen']