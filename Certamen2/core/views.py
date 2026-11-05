from django.shortcuts import render
from .models import Patrimonial
from .models import Categoria

def descripcion(request):

    id_patrimonial = request.GET.get('id')
    patrimonio = Patrimonial.objects.get(id_patrimonial=id_patrimonial)
    data = {
        'elementos': patrimonio,
        'titulo': patrimonio.__str__()
    }

    return render(request,'core/descripcion.html',data)



def inicio(request):

    orden = request.GET.get('orden','id')
    if orden == 'categoria':
        lista = Patrimonial.objects.all().order_by('id_categoria__nombre', 'nombre')
        mensaje = "Volver a orden por defecto"
        url = "?"
    else:
        lista = Patrimonial.objects.all().order_by('id_patrimonial')
        mensaje = "Ordenar por categoría"
        url = "?orden=categoria"

    categoria_id = request.GET.get('categoria')
    if categoria_id:
        lista = lista.filter(
            id_categoria=categoria_id
        )
    categorias = Categoria.objects.all()
        
    data = {
        'titulo': "Nuestro Catálogo",
        'elementos': lista,
        'mensaje': mensaje,
        'url': url,
        'categorias': categorias,
    }    

    return render(request,'core/inicio.html',data)
