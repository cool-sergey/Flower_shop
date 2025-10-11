from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth,messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from users.forms import UserLoginForm, UserRegistrationForm,UserProfileForm
from example.models import Bucket



def login_form(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': UserLoginForm()}
    return render(request, r'Users/login.html', context)

def reg_form(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация произошла успешно')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, r'Users/reg.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance = request.user)
        
    baskets = Bucket.objects.filter(user=request.user)
    total_sum = sum((basket.sum() for basket in baskets))
    total_quantity = sum((basket.quantity for basket in baskets))


    context = {
        'baskets': Bucket.objects.filter(user = request.user),
        'title': 'Store - профиль',
        'form': form,
        'total_sum':total_sum,
        'total_quantity':total_quantity
        
        }
    return render(request, r'Users/profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))