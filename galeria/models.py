from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    
    OPCOES_CATEGORIA = (
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
        
    )
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices= OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', null=False, blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    
    def __str__(self):
        return self.nome

