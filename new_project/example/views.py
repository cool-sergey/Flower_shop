from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from example.models import FlowerType, Product,Bucket



def index(request):
    context ={
        'title':'The Flowers Blog',
        'flowers': Product.objects.all(),
        'type' : FlowerType.objects.all()
        }
    return render(request, r"Example\index.html", context)
#тртетий арг. чтобы можно было встялять данные с помощью слвоворя сразу в шиетмель страницу

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)
def simple(request):
    return render(request,r"Example\simple.html")
def second(request):
    return render(request,r"Example\list.html")

@login_required
def basket_add(request,product_id):
    product = Product.objects.get(id = product_id)
    basket = Bucket.objects.filter(user = request.user,product=product)

    if not basket.exists():
        Bucket.objects.create(user = request.user, product=product, quantity =1)
    else:
        basket = basket.first()
        basket.quantity +=1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
@login_required
def basket_remove(request, basket_id):
    basket = Bucket.objects.get(id = basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER']) 

