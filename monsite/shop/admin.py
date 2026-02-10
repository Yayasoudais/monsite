from django.contrib import admin
from .models import Categorie, Produit, Client

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','slug')
    prepopulated_fields = {'slug':('nom',)}
    
@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom','categorie','prix','prix_promo','stock','disponible','en_vedette')
    list_filter = ('categorie','disponible','en_vedette')
    search_fields = ('nom','description')
    prepopulated_fields = {'slug':('nom',)}
    list_editable = ('prix','stock','disponible','en_vedette') # edition rapide
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom_complet','email','ville','pays','date_inscription')
    search_fields = ('nom','prenom','email')
    list_filter = ('ville','pays','date_inscription')
