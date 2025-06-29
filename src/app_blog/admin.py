from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_creacion')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha_creacion', 'autor', 'categoria')
    autocomplete_fields = ['autor']
    fields = ('titulo', 'slug', 'autor', 'contenido', 'categoria', 'tags', 'publicado')