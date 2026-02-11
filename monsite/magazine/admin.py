from django.contrib import admin
from .models import Auteur, Categorie, Article

# Register your models here.

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'site_web') 
    search_fields = ('nom', 'prenom', 'email')
    
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug') 
    prepopulated_fields = {'slug': ('nom',)}
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'publie', 'vues', 'date_creation') 
    list_filter = ('publie', 'categorie', 'auteur')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}
    list_editable = ('publie',)
# Afficher les ForeignKey comme raw_id (pour beaucoup de données) 

# raw_id_fields = ('auteur', 'categorie')
