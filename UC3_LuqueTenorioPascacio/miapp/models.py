from django.db import models



# Create your models here.

class Curso(models.Model):
    codigo = models.CharField( primary_key=True , max_length=6 )
    nombre = models.CharField( max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)

# Create your models here.