from django.urls import path
from galeria.views import index, imagem

#Criar uma lista de URL's
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]