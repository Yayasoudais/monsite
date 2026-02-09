from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article) 
class ArticleAdmin(admin.ModelAdmin): 
    """Configuration de l"interface admin pour Article"""
    
    # Champs affichés dans la liste 
    
    list_display = ('titre', 'date_publication', 'publie')
    # Champs filtrables 
    
    list_filter = ('publie', 'date_publication')
    
    # Barre de recherche 
    
    search_fields = ('titre', 'contenu')
    
    # Champs remplis automatiquement 
    
    prepopulated_fields = {'slug': ('titre',)}
    
    # Ordre des champs dans le formulaire 
    
    fields = ('titre', 'slug', 'contenu', 'date_publication', 'publie')
    
    # Ou grouper par sections 

    # fieldsets = ( 
    #   ('Informations principales', {
    #     'fields': ('titre', 'slug', 'contenu')
    #   }),
    #   ('Paramètres de publication', {
    #    'fields': ('date_publication', 'publie'')
    #     }),
