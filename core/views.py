from django.shortcuts import render
import requests,json

# Create your views here.

def home (request):
    productos = requests.get('http://127.0.0.1:8000/api/lista-productos')
    datos = productos.json()
    data = {
        'productos':datos
   
    }

    return render(request,'tienda.html',data) 

