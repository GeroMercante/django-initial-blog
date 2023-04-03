from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from blogs.models import Post, Category

# Create your views here.

def home_page(request):
    post = Post.objects.all()
    categorias = Category.objects.all()
    destacado = Post.objects.filter(destacado=True)[:3]

    context = {
        'posts_list': post,
        'categorias': categorias,
        'destacado': destacado
    }

    return render(request, 'blogs/home_page.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post
    # En post, hasta acá, cuando entramos a un slug, no podemos ver las categorias, con la siguiente funcion vamos a poder hacerlo.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Category.objects.all()
        return context
