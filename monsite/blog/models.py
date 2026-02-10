from django.db import models
from django.utils import timezone

# Create your models here.

class Categorie(models.Model): 
    """Catégories pour organiser les articles"""
    
    nom = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField(max_length=100, unique=True) 
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Catégorie" 
        verbose_name_plural = "Catégories" 
        ordering = ['nom']
    
    def __str__(self): 
        return self.nom


class Article(models.Model):
    """"Model représentant un article de blog"""
    
    titre = models.CharField(max_length=200, verbose_name="Titre") 
    slug = models.SlugField(max_length=200, unique=True) 
    contenu = models.TextField(verbose_name="Contenu") 
    
    # NOUVEAU : Relation avec Catégorie (on verra ça demain en détail) 
    
    categorie = models.ForeignKey( 
        Categorie, 
        on_delete = models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='articles',
    )
    
    date_creation = models.DateTimeField(auto_now_add=True) 
    date_modification = models.DateTimeField(auto_now=True) 
    date_publication = models.DateTimeField(default=timezone.now) 
    publie = models.BooleanField(default=False, verbose_name="publié")
    
    class Meta:
    #    verbose_name = "Article" 
    #    verbose_name_plural = "Articles" 
        ordering = ['-date_publication'] # Plus récent en premier
        
    def __str__(self):
        """Représentation textuelle de l'objet""" 
        return self.titre
