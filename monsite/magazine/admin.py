from django.contrib import admin
from .models import Auteur, Categorie, Article, Tag, ProfilAuteur

# Register your models here.

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'site_web') 
    search_fields = ('nom', 'prenom', 'email')
    
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug') 
    prepopulated_fields = {'slug': ('nom',)}
 
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug') 
    prepopulated_fields = {'slug': ('nom',)}
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'publie', 'vues', 'date_creation') 
    list_filter = ('publie', 'categorie', 'auteur','tags')
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug': ('titre',)}
    list_editable = ('publie',)
    filter_horizontal = ('tags',) # Interface améliorée pour ManyToMany

@admin.register(ProfilAuteur)
class ProfilAuteurAdmin(admin.ModelAdmin):
    list_display = ('user', 'ville', 'pays', 'articles_publies', 'date_inscription') 
    search_fields = ('user__username', 'ville')  
    
# Afficher les ForeignKey comme raw_id (pour beaucoup de données) 

# raw_id_fields = ('auteur', 'categorie')
