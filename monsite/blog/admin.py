from django.contrib import admin
from .models import Article, Categorie

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','slug')
    search_fields = ('nom',)
    prepopulated_fields = {'slug':('nom',)}

@admin.register(Article) 
class ArticleAdmin(admin.ModelAdmin): 
    """Configuration de l"interface admin pour Article"""
    
    # Champs affichés dans la liste 
    
    list_display = ('titre','categorie','date_publication','publie')
    
    # Champs filtrables 
    
    list_filter = ('publie','date_publication','categorie')
    
    # Barre de recherche 
    
    search_fields = ('titre','contenu')
    
    # Champs remplis automatiquement 
    
    prepopulated_fields = {'slug': ('titre',)}
    
    # Ordre des champs dans le formulaire 
    
    fields = ('titre', 'slug', 'contenu','categorie', 'date_publication', 'publie')
    
    # Ou grouper par sections 

    # fieldsets = ( 
    #   ('Informations principales', {
    #     'fields': ('titre', 'slug', 'contenu')
    #   }),
    #   ('Paramètres de publication', {
    #    'fields': ('date_publication', 'publie'')
    #     }),
