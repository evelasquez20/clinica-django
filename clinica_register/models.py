from django.db import models

# Create your models here.

class Especialidades(models.Model):
    nombre_especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_especialidad

class Medicos(models.Model):
    nombre_medico = models.CharField(max_length=100)
    jvpm = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField()
    especialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)
