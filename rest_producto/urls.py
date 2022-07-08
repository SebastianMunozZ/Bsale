from django.urls import path
from .views import lista_producto

urlpatterns = [
    path('lista-productos', lista_producto, name='lista_producto'),
]   