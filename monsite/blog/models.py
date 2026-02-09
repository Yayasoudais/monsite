from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    """"Model représentant un article de blog"""
    
    titre = models.CharField(max_length=200, verbose_name="Titre") 
    slug = models.SlugField(max_length=200, unique=True) 
    contenu = models.TextField(verbose_name="Contenu") 
    date_creation = models.DateTimeField(auto_now_add=True) 
    date_modification = models.DateTimeField(auto_now=True) 
    date_publication = models.DateTimeField(default=timezone.now) 
    publie = models.BooleanField(default=False, verbose_name="publié")
    
    class Meta:
        verbose_name = "Article" 
        verbose_name_plural = "Articles" 
        ordering = ['-date_publication'] # Plus récent en premier
        
    def __str__(self):
        """Reprêsentatior textuelle de l'objet""" 
        return self.titre
