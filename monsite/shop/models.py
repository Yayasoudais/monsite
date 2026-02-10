from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Categorie(models.Model):
    """Catégorie de produits""" 
    
    nom = models.CharField(max_length=100) 
    slug= models.SlugField(unique=True) 
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Catégorie" 
        verbose_name_plural = "Catégories"
        ordering = ['nom']
    def __str__(self):
        return self.nom

class Produit(models.Model): 
    """Produit en vente"""
    
    #Informations de base 
    nom = models.CharField(max_length=200) 
    slug= models.SlugField(unique=True) 
    description = models.TextField(blank=True)
    
    #Prix et stock
    prix = models.DecimalField( 
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)]
    )
    
    prix_promo = models.DecimalField(
        max_digits=10,
        decimal_places=2, 
        null=True, 
        blank=True, 
        validators=[MinValueValidator(0)]
    )
    stock = models.PositiveIntegerField(default=0)
    
    # Catégorie
    categorie= models.ForeignKey( 
        Categorie, 
        on_delete=models.CASCADE, 
        related_name= 'produits'
    )
    
    # Caractéristiques
    en_vedette = models.BooleanField(default=False) 
    disponible = models.BooleanField(default=True)
        # Image (nécessite Pillow) 
        #  image = models. ImageField(upload_to='produits/", blank=True)
        
    # Dates
    
    date_ajout = models.DateTimeField(auto_now_add=True) 
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Produit" 
        verbose_name_plural = "Produits" 
        ordering = ['-date_ajout']
    def __str__(self):
        return self.nom
    
    @property
    def prix_final(self):
        """Retourne le prix promotionnel si existant, sinon le prix normal""" 
        return self.prix_promo if self.prix_promo else self.prix
    
    @property 
    def en_stock (self): 
        """Vérifie si le produit est en stock""" 
        return self.stock> 0
    
class Client(models.Model):
    """Client du site""" 
    nom = models.CharField(max_length=100) 
    prenom = models.CharField(max_length=100) 
    email = models.EmailField(unique=True) 
    telephone = models.CharField(max_length=20) 
    adresse = models.TextField() 
    ville = models.CharField(max_length=100) 
    code_postal = models.CharField(max_length=10)
    pays = models.CharField(max_length=100, default='Guinée')
    
    date_inscription = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Client" 
        verbose_name_plural = "Clients"
        
    def _str_(self): 
        return f"{self.prenom} {self.nom}"
    
    @property
    def nom_complet(self): 
        return f"{self.prenom} {self.nom}"