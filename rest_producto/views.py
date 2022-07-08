from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Product, Category
from .serializers import Productoserializer

@csrf_exempt
@api_view(['GET'])
def lista_producto(request):
    """
    GET = Lista todos los productos
    POST = Agrega Registro
    """
    if request.method == 'GET':
        producto = Product.objects.all()
        serializer = Productoserializer(producto, many=True)
        return Response(serializer.data)