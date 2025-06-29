from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado', 'fecha_creacion')
    list_filter = ('publicado', 'fecha_creacion', 'autor')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)