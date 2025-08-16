from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse


from users.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
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
    return render(request, r'Users\login.html', context)

def reg_form(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, r'Users\reg.html',context)