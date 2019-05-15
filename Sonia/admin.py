# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Sonia
from models import Ficha

class SoniaAdmin(admin.ModelAdmin):
    list_display = ['state','day', 'time', 'notes']

admin.site.register(Sonia,SoniaAdmin)

class FichaAdmin(admin.ModelAdmin):
    list_display = ['nombre','telefono','direccion','comienzo', 'dni', 'contrato']

admin.site.register(Ficha,FichaAdmin)