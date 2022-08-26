from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Curso: {self.nombre}. Código: {self.codigo}'