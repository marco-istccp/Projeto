#encoding: utf-8

from django.contrib.auth.models import User
from django.db import models

class ItemAgenda(models.Model):
	data = models.DateField()
	hora = models.TimeField()
	titulo = models.CharField (max_length=100)
	descricao = models.TextField()
	usuario = models.ForeignKey(User)