from django.db import models

# Create your models here.

class Ticket (models.Model):
    numero = models.IntegerField()
    estado = models.BooleanField()
    
    def __str__(self):
        return f'Ticket numero: {self.numero} -Estado{self.estado}'
    
class Tecnico (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edificio = models.CharField(max_length=30)
    
    def __str__(self):
        return f'Tecnico nombre: {self.nombre} -Apellido: {self.apellido} -Email: {self.email} -Edificio: {self.edificio}'
    
class Usuario (models.Model):    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    legajo = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Usuario nombre: {self.nombre} -Apellido: {self.apellido} -Email: {self.email} -Legajo: {self.legajo}'
     