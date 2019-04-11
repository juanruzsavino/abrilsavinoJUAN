# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Tipoproducto(models.Model):
	nombre = models.CharField(max_length=142)


	def __str__(self):
		return 'Tiporoducto {}'.format(self.nombre)    


class Producto(models.Model):
	nombre = models.CharField(max_length=142)
	precio = models.IntegerField()
	tipo_producto = models.ForeignKey(Tipoproducto)


	def __str__(self):
		return 'Producto {} {}'.format(self.nombre , self.precio)    


class Cliente(models.Model):
	nombre = models.CharField(max_length=142)


	def __str__(self):
		return 'Cliente {}'.format(self.nombre)





class Factura(models.Model):
	fecha_de_entrega = models.DateTimeField(editable=True)
	cliente = models.ForeignKey(Cliente)
	producto = models.ForeignKey(Producto)
	cantidad = models.IntegerField(default=1)

	def __str__(self):
		return 'Factura {}'.format(self.cliente.nombre)

