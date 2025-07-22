from django.http import HttpResponse
from django.shortcuts import render

from example.models import FlowerType, Product



def index(request):
    context ={
        'title':'The Flowers Blog',
        'flowers': Product.objects.all(),
        'type' : FlowerType.objects.all()
        }
    return render(request, "Example\main.html", context)
#тртетий арг. чтобы можно было встялять данные с помощью слвоворя сразу в шиетмель страницу

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)
def simple(request):
    return render(request,"Example\simple.html")
def second(request):
    return render(request,"Example\list.html")