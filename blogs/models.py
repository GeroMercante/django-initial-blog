from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    descripcion = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    ingredientes = models.TextField()
    imagen_url = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    categoria = models.ManyToManyField('Category')
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Category(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.titulo
