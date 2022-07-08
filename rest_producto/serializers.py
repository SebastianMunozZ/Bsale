from dataclasses import fields
from rest_framework import serializers
from core.models import Category, Product

class Productoserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name', 'url_image', 'price', 'discount', 'category']