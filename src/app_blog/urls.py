from django.urls import path
from .views import PostListView, PostDetailView

app_name = 'app_blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_lista'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detalle'),
]
