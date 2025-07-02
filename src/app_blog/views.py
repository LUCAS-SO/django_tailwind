from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.utils.text import slugify
from taggit.models import Tag
from .forms import ComentarioForm
from .models import Categoria, Post, Comentario



class CategoriaPostListView(ListView):
    model = Post
    template_name = 'app_blog/categoria_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(
            publicado=True,
            categoria__slug=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.get(slug=self.kwargs['slug'])
        return context
    

class PostPorTagListView(ListView):
    model = Post
    template_name = 'app_blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tags__in=[self.tag], publicado=True).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['categorias_menu'] = Categoria.objects.all()
        return context


class PostListView(ListView):
    model = Post
    template_name = 'app_blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        return Post.objects.filter(publicado=True)
    

class PostDetalleView(FormMixin, DetailView):
    model = Post
    template_name = 'app_blog/post_detail.html'
    context_object_name = 'post'
    form_class = ComentarioForm

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.filter(aprobado=True)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = self.object
            comentario.save()
            return self.form_valid(form)
        return self.form_invalid(form)


class PostsPorTagView(ListView):
    model = Post
    template_name = 'app_blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        tag_slugified = slugify(tag_slug)

        # Buscar el Tag cuyo slugify coincida con el recibido
        tag_obj = next((tag for tag in Tag.objects.all() if slugify(tag.name) == tag_slugified), None)

        if not tag_obj:
            from django.http import Http404
            raise Http404("No Tag matches the given query.")

        self.tag = tag_obj
        return Post.objects.filter(tags__in=[tag_obj], publicado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context