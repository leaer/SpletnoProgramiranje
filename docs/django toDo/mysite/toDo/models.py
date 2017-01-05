from django.db import models
import datetime

PRIORITETA = (
	(1, 'Najmanj pomembno'),
	(2, 'Pomembno'),
	(3, 'Zelo pomembno'),
)

PODROCJE = (
	(1, 'Šola'),
	(2, 'Delo'),
	(3, 'Dom'),
	(4, 'Nakupovanje'),
	(5, 'Ostalo')
)


class Uporabnik(models.Model):
	ime = models.CharField(max_length=30)
	priimek = models.CharField(max_length=30)
	uporabniskoIme=models.CharField(max_length=20)
	geslo=models.CharField(max_length=30)
	zadnjaPrijava=models.DateTimeField()
	pass
	
	def __str__(self):
		return self.uporabniskoIme        

class Opravilo(models.Model):
	uporabnik = models.ForeignKey(Uporabnik, on_delete=models.CASCADE)
	ime = models.CharField(max_length=200)
	createDate = models.DateTimeField(default=datetime.datetime.now)
	dueDate = models.DateTimeField(default=datetime.datetime.now)
	prioriteta = models.CharField(max_length=20,choices=PRIORITETA, default=1)
	podrocje = models.CharField(max_length=20, choices=PODROCJE, default=1)
	zapiski = models.CharField(max_length=400)
	opravljen = models.BooleanField(default=False)
	
	

	