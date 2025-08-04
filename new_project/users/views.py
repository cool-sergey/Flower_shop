from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_form(request):
    return render(request, 'Users\login.html')

def reg_form(request):
    return render(request, r'Users\reg.html')