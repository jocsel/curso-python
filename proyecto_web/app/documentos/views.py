# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from documentos.models import Documento

# Create your views here.
from django.views.generic import View
class Documentos(View):
    def get(self, request, *args, **kwargs):
        docs = Documento.objects.all()
        #SELECT * FROM documentos_documentos
        context = {
            'docs':docs,
            'encabezado': 'Mis Documentos'
        }
        return render(request,'documentos.html',context)


