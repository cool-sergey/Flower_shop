from django.urls import path
from example import views


app_name = 'example'

urlpatterns = [    
    #path(' ', views.shop) типо магазин цветов , с карточками и отзывами на них
    path('about/', views.about, kwargs={'name':'Tom', 'age': 38}),
    path('simple/',views.simple, name='simple'),
    path('list/',views.second,name='list'),
    path('basket/add/<int:product_id>/', views.basket_add, name='busket_add'),
    path('basket/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),

]
