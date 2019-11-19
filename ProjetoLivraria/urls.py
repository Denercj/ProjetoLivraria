
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('livraria/',include('AppLivraria.urls')),
    path('admin/', admin.site.urls),
]
