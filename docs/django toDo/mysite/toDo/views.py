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

#VIEWS

def index(request):
#	Funkcija 'index' vraca prvo stran, ki je vidna tistim, ki niso vpisani ali registrirani.
#	Izgled in postavitev strani se nahaja v html datoteki home.html (Templates), za oblikovanje pa poskrbi 'ToDo.css' (Static).

	return render(request, 'toDo/home.html')
	
#opravila
def opravila(request):
#    Funkcija "opravila" preveri, ce je uporabnik avtenticiran. Ce je, se na strani preglejOpravila prikazejo vsa opravila vpisanega uporabnika. Vsa opravila vpisanega uporabnika shrani v "vsa_opravila".	
#	@vsa_opravila - spremenljivka, kamor shrani vsa opravila vpisanega uporabnika	
#	Izgled in postavitev strani 'preglejOpravila' se nahaja v html datoteki preglejOpravila.html (Templates), za oblikovanje pa poskrbi 'opravila.css' (Static).
#	Opravila so razporejena glede na datum, podrocje ter prioriteto. 

	if request.user.is_authenticated():
		vsa_opravila = Opravilo.objects.filter(uporabnik=request.user)
		context = {'vsa_opravila': vsa_opravila}
	else:
		context = {'title': "Vpiši se"}
	return render(request, 'toDo/preglejOpravila.html', context)

def opravila_dodaj(request):
#   Funkcija "opravila_dodaj" poskrbi za dodajanje opravil. v spremenljivki form hranim formo, ki sem jo spisala v "forms.py" - OpraviloForm.  OpraviloForm vsebuje polja za vnos imena opravila, datum in uro, do kdaj mora biti opravilo dokoncano, podrocje, prioriteto ter zapiske o opravilu.
#	Ce je forma za dodajanje opravila pravilno izpolnjena (obvezna so vsa polja razen zapiskov), se ob kliku na gumb "Dodaj" opravilo shrani med opravila vpisanega uporabnika, uporabnika pa preveze na stran "preglejOpravila", kjer so zapisana vsa njegova opravila.
#	Logger preverja, kaj je vneseno v formo za dodajanje. 
#	@form - variabla, kamor se shrani OpraviloForm
#	@opr - variabla, kamor se shrani Opravilo z novimi vnosi.Z opr.save() se opravilo shrani v bazo
#	Izgled in postavitev strani, kjer uporabnik izpolnjuje formo za dodajanje opravila, se nahaja v html datoteki 'opravila.html' (Templates), za oblikovanje poskrbi 'opravila.css'(Static).
	
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
#   Funkcija "OpraviloUpdate" omogoci posodablanje ze vpisanega opravila. Na strani 'uredi_Opravilo', do katere uporabnik dostopa s klikom na samo opravilo na strani 'preglejOpravila', je forma, ki vsebuje taksna polja, kot forma za dodajanj opravil. Razlika je, da so tu polja ze izpolnjena z vnosi za to doloceno opravilo, katerega uporabnik zeli spremeniti. Uporabnik lahko spremeni vnose, lahko tudi oznaci opravilo kot opravljeno in s klikom na gumb 'Posodobi' nove podatke shrani v bazo.
#	Ce je forma pravilno izpolnjena, se novi podatki shranijo (form.save()). Po tem redirecta na stran, kjer uporabnik lahko pregleduje svoja opravila.
#	@instance - variabla, kamor se shranijo podatki opravila, ki ga porabnik zeli posodobiti (opravilo z dolocenim id-jem).
#	@form - variabla, kamor se shrani forma UrediOpraviloForm, ki vsebuje podatke opravila, ki ga zelimo posodobiti.
#	Izgled in postavitev strani, kjer uporabnik posodablja zeleno opravilo, se nahaja v html datoteki 'uredi_opravilo.html' (Templates), za oblikovanje poskrbi 'opravila.css' (Static).

	instance = Opravilo.objects.get(id=id)
	form = UrediOpraviloForm(request.POST or None, instance=instance)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('preglej_opravila'))
	return render(request, 'toDo/uredi_opravilo.html', {'form': form, 'id':id})
	
def OpraviloDelete(request,id):
#	Funkcija "OpraviloDelete" poskrbi za brisanje zelenega opravila. Uporabnik se lahko odloci za brisanje opravila na strani, kjer ureja opravilo. 
#	S klikom na gumb 'Brisi opravilo' uporabnika preveze na stran, kjer ga stran se enkrat vprasa, ce res zeli izbrisati opravilo. S klikom na gmb 'Brisi', je opravilo izbrisano iz baze.
#	@instance - variabla, kamor se shrani id opravila, ki ga zelimo izbrisati. Iz baze se nato izbrise opravilo s tem id-jem.
#	Izgled in postavitev strani, kjer uporabnik brise zeleno opravilo, se nahaja v html datoteki 'brisi_opravilo.html' (Templates), za oblikovanje poskrbi 'opravila.css' (Static).

	instance = get_object_or_404(Opravilo, id=id)
	form = OpraviloForm(request.POST or None, instance=instance)
	if request.method == 'POST':
		instance.delete()
		return HttpResponseRedirect(reverse('preglej_opravila'))
	return render(request, 'toDo/brisi_opravilo.html', {'form': form, 'id':id})
	
def opravljena_opravila(request):
#	Funkcija 'opravljena_opravila' omogoci uporabniku pregled opravil, ki jih je ze opravil. Funkcija vraca vsa opravila vpisanega uporabnika, v html datoteki pa je spisano, da na strani 'opravljenaOpravila' prikaze zgolj opravila, ki so oznacena kot opravljena ({{Opravilo.opravljen == True}}).

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
#	Funkcija 'uporabnik' omogoca le-temu, da pregleda svoje podatke, ki jih je nastavil ob registraciji.  Podatke mu izpise na strani 'uporabnik'.
#	Izgled in postavitev strani, kjer uporabnik pregleduje svoje podatke, se nahaja v html datoteki 'uporabnik.html' (Templates), za oblikovanje poskrbi 'opravila.css' (Static).
	if request.user.is_authenticated():
		podatkiOuporabniku = request.user
		context = {'podatkiOuporabniku': podatkiOuporabniku}
	else:
		context = {'title': "Vpiši se"}
	return render(request, 'toDo/uporabnik.html', context)	
	
def uredi_uporabnika(request):
#   Funkcija uredi_uporabnika poskrbi, da uporabnik lahko posodobi podatke, ki jih je vpisal ob registraciji. Ko na strani uporabnik pritisne n gumb 'Uredi profil', ga usmeri na stran 'urediUporabnika'. Ce uporabnik formo pravilno izpolni, se le ta shrani, uporabnika pa preveze nazaj na stran 'uporabnik'.
#	@EditProfileForm - forma, kjer so ze vpisani podatki uporabnika, ki je vpisan (uporabnika dobimo s klicom request.user), to formo uporabnik ureja
#	Izgled in postavitev strani, kjer uporabnik ureja svoje podatke, se nahaja v html datoteki 'uredi_uporabnika.html' (Templates), za oblikovanje poskrbi 'opravila.css' (Static).

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
#   Funkcija 'prijava' omogoca prijavo uporabnika. Na strani 'prijava' se mu prikaze forma za vpis uporabniskega imena in gesla (LoginForm). Ce je forma pravilno izpolnjena, se uporabnika avtenticira in ga vpise. Ko se vpise, ga preveze na stran, kjer so vidna vsa njegova opravila.	
#	Izgled in postavitev strani, kjer se uporabnik vpisuje, se nahaja v html datoteki 'prijava.html' (Templates), za oblikovanje poskrbi 'opravila.css' (Static).

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
#	Funkcija 'logout' poskrbi, da se uporabnik lahko izpise. Izpise se ob kliku na gumb 'Odjava'. Ko se uporabnik odjavi, ga redirecta na prvo stran, tj. 'index'.

    logout(request)
    return HttpResponseRedirect('toDo/logout')
	
def registracija(request):	
#	Ce uporabnik se ni registriran, to lahko stori zaradi funkcije 'registracija'. Na prvi strani (index) lahko izbere moznost registracije. Izpolniti mora formo 'RegistrationUser', ki ima polja uporabnisko ime, ime, priimek, email ter geslo. Ko pritisne na gumb 'Registriraj se', se uporabnika doda v bazo, prav tako ga avtomaticno ze vpise v stran, prijava ni potrebna. Preveze ga na stran 'preglej_opravila'.
#	Izgled in postavitev strani, kjer se uporabnik registrira, se nahaja v html datoteki 'registracija.html' (Templates), za oblikovanje poskrbi 'opravila.css' (Static).

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