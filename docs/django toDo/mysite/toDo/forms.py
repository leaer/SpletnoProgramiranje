from django.contrib.auth.models import User
from django import forms
from .models import Uporabnik, Opravilo
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

#FORMS

class UserForm(forms.Form):

#	Razred, kjer so dolocena polja, ki jih ima uporabnik. Uporabila sem User-ja, ki ga lahko dobimo od Djangota z importom django.contrib.auth.models import User. 
#	Vsebuje polja username, first_name, last_name, email, password. Model, ki je uporabljen, kot ze receno ni model form (lastno zgrajen), ampak forma User.

	username=forms.CharField(max_length=20)
	first_name=forms.CharField(max_length=20)
	last_name=forms.CharField(max_length=20)
	email=forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class RegistrationUser(UserCreationForm):
#	V razredu RegistrationForm zgradim formo za registracijo uporabnika. Forma za registracijo vsebuje ista polja, kot sem jih nastela v razredu UserForm.
#	Uporabila sem Djangovo privzeto funkcijo za ustvarjanje Userja - UserCreationForm, ki sem jo uvozila (from django.contrib.auth.forms import UserCreationForm).

	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']


#	Razred vsebuje se funkcijo save, ki shrani uporabnika v bazo.


	def save (self, commit=True):
		user = super(RegistrationUser, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		
		if commit: 
			user.save()
		return user
		

class OpraviloForm(forms.ModelForm):
#	V tem razredu se naredi forma za opravilo, ki vsebuje ime opravila, datum, do kdaj je potrebno opravilo opraviti, prioriteto, podrocje ter zapiske.
#	Model, po katerem je forma ustvarjena, je model Opravilo, ki sem ga spisala sama in se nahaja v models.py.

	class Meta:
		model = Opravilo
		fields =  ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski']

class LoginForm(forms.Form):
#	v razredu 'LoginForm' se naredi forma za vpis uporabnika, ki vsebuje polji username in password. Model, ki je uporabljen, je User.

	username=forms.CharField(max_length=20)
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['username', 'password']

class EditProfileForm(UserChangeForm):

#	V razredu 'EditProfileForm' se ustvari forma za urejanje uporabnikovega profila. Forma za urejanje vsebuje enaka polja kot forma za registracijo uporabnika, model je User.
#	Tudi tukaj sem uporabila Djangovo funkcijo za urejanje uporabnika - UserChangeForm, ki sem jo uvozila (from django.contrib.auth.forms import UserChangeForm).

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UrediOpraviloForm(forms.ModelForm):
#	V razredu 'UrediOpraviloForm' se naredi forma za urejanje opravila, ki vsebuje taksna polja, kot forma za dodajanje opravila, dodano je se, da uporabnik oznaci, ce je opravilo opravljeno ali ne.
#	Model je Opravilo.

	class Meta:
		model = Opravilo
		fields = ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski', 'opravljen']
		
class BrisiOpraviloForm(forms.ModelForm):
#	 V razredu 'BrisiOpraviloForm' se naredi forma za brisanje opravila, vsebje polja kot jih ima forma za dodajanje opravil oz. kot jih ima model Opravilo. 

	class Meta:
		model = Opravilo
		fields = ['ime', 'dueDate', 'prioriteta', 'podrocje', 'zapiski']