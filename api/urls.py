from django.urls import path
from .views import (
    CategoriaListView, CategoriaDetailView,
    ProductoListView, ProductoDetailView,
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
]
