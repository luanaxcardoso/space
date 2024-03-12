from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.db.models import Q
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria.')
        return redirect('login')
        
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar a galeria.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    nome_a_buscar = ''

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(Q(nome__icontains=nome_a_buscar) | Q(nome__icontains=nome_a_buscar.capitalize()))
    
    return render(request, 'galeria/buscar.html', {'cards': fotografias, 'buscar': nome_a_buscar})