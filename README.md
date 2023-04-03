# Incialización del proyecto. Paso a paso.

## Entorno virtual:
- `virtualenv env -> activamos el env`

## Instalación de Django:
- `pip install django`

## Creando el proyecto de Django:
- `django-admin startproject core .`

## Creando apps:
- `python manage.py startapp users`

## Creando modelos de usuarios:
- `Use el AbstractUser de django como modelo idoneo para el usuario`

## Desplegando el Blog:
- `En el models.py creamos la clase Post, que tiene un título, y un slug, el slug, nos va a permitir generar url unicas gracias a su propiedad SlugField(unique=True), seteado en true por supuesto. un DateTime automatico en el momento que se crea un Post. Tambien podemos observar una propiedad de: author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT), que lo que tambien pudimos haber hecho, ya que nosotros tenemos un modelo de usuario, es importar ese modelo de usuario y pasarle como primer parametro la clase User, pero, cuando queremos modificar algo, o subir un Post, tendriamos que cambiar varias cosas, entonces con el AUTH_USER_MODEL que declaramos en el settings.py, nos ahorra demasiados cambios.`




css
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

js
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
