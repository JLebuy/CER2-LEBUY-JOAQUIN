# CER2-LEBUY-JOAQUIN
Repositorio de Certamen 2 TLP


En cmd o terminal VS ->
 
Instalar y actualizar servicios necesarios
1. Verificar que python esté instalado
   python --version
2. Verificar que PIP esté instalado
   py -m pip --version
3. Actualizar PIP de ser necesario
   py -m pip install --upgrade pip
4. Instalar Django
   pip install django
   py -m django --version

Luego creamos el directorio de proyectos
cd\ (dirigirse a la ubicación deseada o carpeta de 
proyectos)
*md (nombre del directorio)
*cd (nombre del directorio)
*c:\(nombre del directorio) (dentro de la carpeta)

Creación de la carpeta de proyectos:
django-admin startproject (nombre de proyecto)




En VSCODE (terminal) ->

Creación de una aplicación (nuestro sitio web):
1 django-admin startapp (nombre de app) 	o
2 py manage.py startapp (nombre de app)

En el archivo settings.py debemos agregar el nombre
de la aplicación creada a INSTALLED_APPS

Iniciar servidor:
py manage.py runserver
(el servidor no debe mantenerse activo durante el uso 
de la aplicación)

Para ver el resultado:
http://127.0.0.1:8000/




Configuraciones básicas ->

1. En views.py se definirán las funciones que llamen
   a los templates de páginas:
def nombre(request):
   return render(request,'core/nombre.html')


2. En urls.py se debe importar views y luego agregar
la ruta a la función respectiva definida en views:
-from (aplicación) import views
-path('nombre/',views.nombre,name='nombre'),
 (dentro de urlpatterns, que es una lista)


3. Crear un archivo .html dentro de /core/templates/core


4. Definir elementos en views y meterlos en un 
diccionario y colocar este como un contexto del 
argumento de la función en views. Eso nos permitirá
definir partes de la página dinámicamente:
-data = {
        'titulo': titulo,
       	'elementos': coleccion,
}
-def nombre(request):
   return render(request,'core/nombre.html',ctexto/data)


5. Insertar bloques de texto Python dentro del código
de la página HTML: 
{% for elemento in elementos %} para bucles
(se terminan con {% endfor %}),
{{elemento}} para hacer un "print" y
{% static 'core/img/imagen' %} para importar
elementos estáticos (CSS, JS, imágenes, etc)
(se debe crear una carpeta static dentro de /core y 
dentro las carpetas que sean necesarias eg: CSS/JS/PNG):
{% load static %} (al inicio)
{% static 'core/css/bootstrap.css' %} (dentro del link)


6. Editar archivos 1) models.py y 2) admin.py

1)
Crear clase con atributos y sus propiedades y además
un método que permita reunir los atributos y mostrarlos
en pantalla (toString):

class Carrera(models.Model):
    codigo = models.CharField(max_length=6, 
    primary_key=True)
    nombre = models.CharField(max_length=60)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre + " (" + str(self.duracion) 
        + " semestres)"

2)
Importar la clase definida en .models y con eso crear
otra clase que defina las vistas de admin (orden de
presentación, criterio de ordenamiento, etc):

from .models import Carrera

class CarreraAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','duracion']
    ordering = ['duracion']

admin.site.register(Carrera,CarreraAdmin)


7. Realizar migraciones (Se debe hacer cada vez que se
modifica el archivo models.py):
 - py manage.py makemigrations
 - py manage.py migrate
 - py mange.py createsuperuser (solo se hace una vez)


8. Acceder a la ip, en la página de administración 
(127.0.0.1/admin) y loguearse con los datos de usuario
usados al crear un perfil de superusuario.
Con eso se pueden añadir/borrar/editar/consultar datos a
la clase definida en models.py usando interfaz gráfica


9. En views.py se debe importar la clase de models y
colocar sus atributos como contexto de la función return
que luego se mostrarán en la página con ayuda de la 
función toString() definida antes:

from .models import (Clase)

(Dentro de la función)
lista_x = (Clase).objects.all().order_by('nombre')
