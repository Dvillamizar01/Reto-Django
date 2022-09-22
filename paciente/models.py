from django.db import models
class paciente(models.Model):  
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=5)
    peso = models.CharField(max_length=15)
    frecuencia_cardiaca = models.CharField(max_length=15)
    spo2 = models.CharField(max_length=15)
    nivel_estres = models.CharField(max_length=15)
    class Meta:  
        db_table = "paciente"