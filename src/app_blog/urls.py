from django.urls import path
from .views import CategoriaPostListView, PostListView, PostDetailView, PostPorTagListView

app_name = 'app_blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_lista'),
    path('categoria/<slug:slug>/', CategoriaPostListView.as_view(), name='categoria_posts'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detalle'),
    path('tag/<slug:slug>/', PostPorTagListView.as_view(), name='post_por_tag'),
]
