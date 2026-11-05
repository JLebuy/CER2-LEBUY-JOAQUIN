from django.db import models

class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Patrimonial(models.Model):

    id_patrimonial = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=120)
    ubicacion = models.CharField(max_length=70)
    anio_construccion = models.DateField()
    imagen = models.ImageField(blank=True)
    id_categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "Nombre: " + self.nombre