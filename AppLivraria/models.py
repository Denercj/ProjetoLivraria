from django.db import models

class Livro(models.Model):
    
    titulo = models.CharField(max_length=255, null=False, blank=False)
    autor = models.CharField(max_length=255, null=False, blank=False)
    editora = models.CharField(max_length=255, null=False, blank=False)
    numero_paginas = models.IntegerField(default=0, null=False, blank=False)
    preco = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
    
objetos = models.Manager()