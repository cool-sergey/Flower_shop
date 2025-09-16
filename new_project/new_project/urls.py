from django.urls import path,include
from example import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('flowertype/<int:flowertype_id>/', views.index, name='flowertype'),
    path('page/<int:page_number>/', views.index, name='paginator'),    

    path('example/', include('example.urls', namespace='example')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
