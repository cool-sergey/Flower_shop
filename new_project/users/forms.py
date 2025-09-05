from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms 
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))    

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Подтвердите пароль'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите адрес электронной почты'
    }))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control-profile', 'placeholder': 'Введите имя пользователя'
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control-profile', 'placeholder': 'Введите имя пользователя'
    }),required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control-profile', 'placeholder': 'Введите адрес электронной почты'
    }),required=False)

    class Meta:
        model = User
        fields = ('username','image','email')