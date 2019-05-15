# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.db import models

NUM_CHOICES = (
	('Salida','Salida'),
	('Entrada', 'Entrada'),
)
class Sonia(models.Model):
	state = models.CharField(max_length=20, choices=NUM_CHOICES, default='Salida')
	day = models.DateField(u'Día', help_text=u'Día')
	time = models.TimeField(u'Hora', help_text=u'Hora')
	notes = models.TextField(u'Observaciones', help_text=u'Observaciones', blank=True, null=True)
 
	class Meta:
		verbose_name = u'Horario'
		verbose_name_plural = u'Horario'

class Ficha(models.Model):
	nombre = models.CharField(max_length=120)
	telefono = models.FloatField(null=True, blank=True)
	direccion = models.CharField(max_length=120,null=True, blank=True)
	comienzo = models.DateTimeField(auto_now_add=True)
	dni = models.FileField(null=True, blank=True)
	contrato = models.FileField(null=True, blank=True)

	class Meta:
		verbose_name = u'Ficha'
		verbose_name_plural = u'Ficha'
