from django.contrib import admin
from .models import Patrimonial
from .models import Categoria

class PatrimonialAdmin(admin.ModelAdmin):

    list_display = ['id_patrimonial','nombre','descripcion','ubicacion','anio_construccion','imagen','id_categoria']
    ordering = ['id_patrimonial']

admin.site.register(Patrimonial,PatrimonialAdmin)

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['id_categoria','nombre','descripcion']
    ordering = ['id_categoria']

admin.site.register(Categoria,CategoriaAdmin)