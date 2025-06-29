from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


User = get_user_model()


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('app_blog:categoria_posts', kwargs={'slug': self.slug})


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    contenido = models.TextField()
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(
    Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = TaggableManager(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo)
            slug = base_slug
            num = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('app_blog:post_detalle', kwargs={'slug': self.slug})