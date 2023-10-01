from django.db import models

# Create your models here.
class Estudiante(models.Model):
    numero_de_estudiante = models.PositiveBigIntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    campo_de_estudio = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Estudiante: {self.nombre} {self.apellido}'
