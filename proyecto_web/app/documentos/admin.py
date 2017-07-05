# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from documentos.models import Documento

class DocumentoAdmin(admin.ModelAdmin):
	model = Documento
admin.site.register(Documento, DocumentoAdmin)