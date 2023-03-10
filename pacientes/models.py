from django.db import models


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
