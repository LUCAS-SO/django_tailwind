from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    contenido = models.TextField()
    publicado = models.BooleanField(default=False)
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