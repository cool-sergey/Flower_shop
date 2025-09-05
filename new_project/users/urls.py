from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [    

    path('login/', views.login_form, name='login'),
    path('reg/', views.reg_form, name = 'reg'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.logout, name = 'logout'),
]
