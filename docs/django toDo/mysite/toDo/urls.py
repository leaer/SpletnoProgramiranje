from django.conf.urls import url, include
from . import views
from django.contrib import admin
app_name='toDo'


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^list/$', views.opravilo_list, name='list'),
	url(r'^$', views.index, name='index'),
	url(r'prijava', views.prijava, name='prijava'),
	url(r'^logout/', views.logout, name='logout'),
	url(r'opravila/', views.opravila, name ='preglej_opravila'),
	url(r'urediOpravilo/(?P<id>[0-9]+)/', views.OpraviloUpdate, name ='uredi_opravilo'),
	url(r'opravljenaOpravila/', views.opravljena_opravila, name ='opravljena_opravila'),
	#url(r'urediOpravilo/', views.OpraviloUpdate, name='uredi_opravilo'),
	url(r'dodajOpravila', views.opravila_dodaj, name='dodaj_opravilo'),
	url(r'/(?P<id>[0-9]+)/brisiOpravilo/', views.OpraviloDelete, name='brisi_opravilo'),
	url(r'^registracija/', views.registracija, name='registracija'),
	url(r'^uporabnik', views.uporabnik, name='uporabnik'),
	url(r'^urediUporabnika', views.uredi_uporabnika, name='uredi_uporabnika')
]
