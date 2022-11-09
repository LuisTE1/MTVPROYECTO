from django.db import models

# Create your models here.
class Familiares(models.Model):
    
    #columnas o campos     
     celular = models.IntegerField()
     nombre = models.CharField(max_length=50)
     parentesco = models.CharField(max_length=50)
     
class Family(models.Model):
    
    #columnas o campos     
     celular = models.IntegerField()
     nombre = models.CharField(max_length=50)
     parentesco = models.CharField(max_length=50)
     fecha_nacimiento = models.DateField()