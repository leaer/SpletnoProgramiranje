from django.conf.urls import url, include
from . import views
from django.contrib import admin


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^list/$', views.opravilo_list, name='list'),
	url(r'^$', views.index, name='index'),
	url(r'opravila', views.opravila, name ='preglej_opravila'),
	url(r'dodajOpravila', views.opravila_dodaj, name='dodaj_opravilo'),
	url(r'^registracija/', views.UserFormView.as_view(), name='registracija')
]
