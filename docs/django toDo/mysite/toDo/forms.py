from django.contrib.auth.models import User
from django import forms
from .models import Uporabnik, Opravilo
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class UserForm(forms.Form):
	username=forms.CharField(max_length=20)
	first_name=forms.CharField(max_length=20)
	last_name=forms.CharField(max_length=20)
	email=forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class RegistrationUser(UserCreationForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']
	
	def save (self, commit=True):
		user = super(RegistrationUser, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		
		if commit: 
			user.save()
		return user
		

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
		
class BrisiOpraviloForm(forms.ModelForm):
	class Meta:
		model = Opravilo
		fields = ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski']