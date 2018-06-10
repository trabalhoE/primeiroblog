from django.db import models
from django.utils import timezone


class Especie(models.Model):
	Especie= models.CharField(max_length=200)
	Descricao= models.TextField()

	def __str__(self):
		return self.Especie




class Genero(models.Model):
	Genero= models.CharField(max_length=200)
	Descricao= models.TextField()

	def __str__(self):
		return self.Genero








class Familia(models.Model):
	Familia = models.CharField(max_length=200)
	Descricao= models.TextField()

	def __str__(self):
		return self.Familia



class ClassificacaoTaxonomica(models.Model):
	Familia= models.ForeignKey(
		'Familia',
		on_delete=models.CASCADE )
	Genero= models.ForeignKey(
		'Genero',
		on_delete=models.CASCADE)
	Especie= models.ForeignKey(
		'Especie',
		on_delete=models.CASCADE)
	
	
	
		