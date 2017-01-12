from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import RegistrationUser, UserForm, OpraviloForm, LoginForm, UrediOpraviloForm, EditProfileForm, BrisiOpraviloForm
#from django.forms.models import model_to_dict
from .models import Opravilo, Uporabnik
from django.views.generic.edit import UpdateView
from django.urls import reverse
import logging

Logger = logging.getLogger(__name__)

def index(request):
	return render(request, 'toDo/home.html')
	
#opravila
def opravila(request):
	if request.user.is_authenticated():
		vsa_opravila = Opravilo.objects.filter(uporabnik=request.user)
		context = {'vsa_opravila': vsa_opravila}
	else:
		context = {'title': "Vpiši se"}
	return render(request, 'toDo/preglejOpravila.html', context)

def opravila_dodaj(request):
	form = OpraviloForm(request.POST or None)
	if request.POST:
		print(request.POST)
		if form.is_valid():
			opr = Opravilo(ime=form.cleaned_data['ime'],dueDate=form.cleaned_data['dueDate'],
				prioriteta=form.cleaned_data['prioriteta'],podrocje=form.cleaned_data['podrocje'],zapiski=form.cleaned_data['zapiski'],opravljen=False,uporabnik=request.user)
			opr.save()
			return HttpResponseRedirect('opravila')
	context= {'form': form}
	Logger.debug("msg")
	return render(request,'toDo/opravila.html',context)

def OpraviloUpdate(request,id):
	instance = Opravilo.objects.get(id=id)
	form = UrediOpraviloForm(request.POST or None, instance=instance)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('preglej_opravila'))
	return render(request, 'toDo/uredi_opravilo.html', {'form': form, 'id':id})
	
def OpraviloDelete(request,id):
	instance = get_object_or_404(Opravilo, id=id)
	form = OpraviloForm(request.POST or None, instance=instance)
	if request.method == 'POST':
		instance.delete()
		return HttpResponseRedirect(reverse('preglej_opravila'))
	return render(request, 'toDo/brisi_opravilo.html', {'form': form, 'id':id})
	
def opravljena_opravila(request):
	if request.user.is_authenticated():
		vsa_opravila = Opravilo.objects.filter(uporabnik=request.user)
		context = {'vsa_opravila': vsa_opravila}
	else:
		context = {'title': "Vpiši se"}
	return render(request, 'toDo/opravljena_opravila.html', context)

def opravilo_list(request):
	vsi_uporabniki = Uporabnik.objects.all()
	return render(request, context)	
	
#uporabnik
def uporabnik(request):
	if request.user.is_authenticated():
		podatkiOuporabniku = request.user
		context = {'vsa_opravila': podatkiOuporabniku}
	else:
		context = {'title': "Vpiši se"}
	return render(request, 'toDo/uporabnik.html', context)	
	
def uredi_uporabnika(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('uporabnik')
    else:
        form = EditProfileForm(instance=request.user)

    context= {'form': form}
    return render(request, 'toDo/uredi_uporabnika.html', context)
	
def prijava(request):
	if request.method=='POST':
		form = LoginForm(request.POST or None)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('opravila')
	else:
		form = LoginForm()
	return render(request, 'toDo/prijava.html', {'form': form})
	
def logout(request):
    logout(request)
    return HttpResponseRedirect('toDo/logout')
	
def registracija(request):	
	if request.method == 'POST':
		form = RegistrationUser(request.POST or None)
		if form.is_valid():
			form.save()
			user = authenticate(username=form.cleaned_data['username'],first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('preglej_opravila'))
		else:
			return render(request, 'toDo/registracija.html', {'form': form})
	else:
		form = RegistrationUser()
		return render(request, 'toDo/registracija.html', {'form': form})