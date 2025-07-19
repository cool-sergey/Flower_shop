from django.http import HttpResponse
from django.shortcuts import render
  
def index(request):
    context ={
        'title':'The Flowers Blog',
        'flowers': [
            {
            'image': 'static/pic/flower1.jpg',
            'alt': 'Цветок зеленый',
            'name':'зеленая орхидея',
            'price':9
            },
            {
            'image': 'static/pic/flower2.jpg',
            'alt': 'гладиолус',
            'name':'гладиолус',
            'price':7
            },
            {
            'image': 'static/pic/flower3.jpg',
            'alt': 'Лагурус',
            'name':'Лагурус',
            'price':5
            },
            {
            'image': 'static/pic/flower4.jpg',
            'alt': 'Хризантема одноголовая',
            'name':'Хризантема одноголовая',
            'price':11
            },
            {
            'image': 'static/pic/flower5.jpg',
            'alt': 'Гортензия лимонная',
            'name':'Гортензия лимонная',
            'price':10
            }
            ]
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