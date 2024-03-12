from django.urls import path
from apps.galeria.views import index, imagem, buscar

#Criar uma lista de URL's
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
]