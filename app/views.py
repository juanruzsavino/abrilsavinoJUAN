# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import *


def factura(request):
	factura = Factura.objects.all()
	return render(request, 'factura.html', {'diccionario': factura})


