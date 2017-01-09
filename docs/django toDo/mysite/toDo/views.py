from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import UserForm, OpraviloForm
from .models import Opravilo, Uporabnik
import logging

Logger = logging.getLogger(__name__)


def index(request):
	return render(request, 'toDo/home.html')
	
def opravila(request):
	if request.user.is_authenticated():
		vsa_opravila = Opravilo.objects.all()
		context = {'vsa_opravila': vsa_opravila}
	else:
		context = {'title': "Vpiši se"}
	return render(request, 'toDo/preglejOpravila.html', context)

def opravila_dodaj(request):
	form = OpraviloForm(request.POST or None)
	if request.POST:
		print(request.POST)
		if form.is_valid():
			opr = Opravilo(ime=form.cleaned_data['ime'],createDate=form.cleaned_data['createDate'],dueDate=form.cleaned_data['dueDate'],
				prioriteta=form.cleaned_data['prioriteta'],podrocje=form.cleaned_data['podrocje'],zapiski=form.cleaned_data['zapiski'],opravljen=False,uporabnik=request.user)
			opr.save()
			return HttpResponseRedirect('toDo/opravila.html')
	context= {'form': form}
	Logger.debug("msg")
	return render(request, 'toDo/opravila.html', context)

def opravilo_list(request):
	vsi_uporabniki = Uporabnik.objects.all()
	return render(request, context)	
	
class UserFormView(View):
	form_class = UserForm
	template_name = 'toDo/registracija.html'
	
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
	
	def post(self,request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			user = form.save(commit=False) #ustvari objekt iz forma, vendar ne shrani v bazo
			ime = form.cleaned_data['ime']
			priimek = form.cleaned_data['priimek']
			email = form.cleaned_data['email']
			uporabniskoIme = form.cleaned_data['uporabnisko ime']
			geslo = form.cleaned_data['geslo']
			#user.set_password(password)
			user.save() #shrani v bazo
	
			user = authenticate(uporabniskoIme=uporabniskoIme, geslo = geslo)
			
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('toDo/home')

