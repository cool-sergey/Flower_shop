from django.urls import path,include
from example import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, kwargs={'name':'Tom', 'age': 38}),
    path('simple/',views.simple, name='simple'),
    path('list/',views.second,name='list'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
