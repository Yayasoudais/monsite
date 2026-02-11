from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Auteur(models.Model):
    """Auteur d'articles"""
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    date_naissance = models.DateField(null=True, blank=True) 
    site_web = models.URLField(blank=True)
    
    class Meta:
        verbose_name = "Auteur" 
        verbose_name_plural = "Auteurs" 
        ordering = ['nom', 'prenom']
        
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

class Categorie(models.Model):
    """Catégorie d'articles"""
    
    nom = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Catégorie" 
        verbose_name_plural = "Catégories"
    def __str__(self): 
        return self.nom


class Tag(models.Model):
    """Tag pour catégoriser les articles"""
    nom = models.CharField(max_length=50, unique=True) 
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Tag" 
        verbose_name_plural = "Tags" 
        ordering = ['nom']
        
    def __str__(self): 
        return self.nom


class ProfilAuteur(models.Model):
    """Profil étendu d'un auteur (lié au User Django)"""
    # RELATION OneToOne
    user = models.OneToOneField( 
        User,
        on_delete=models.CASCADE,
        related_name='profil_auteur' 
    )
    
    # Informations supplémentaires
    bio = models.TextField(blank=True)
    # photo = models.ImageField(upload_to='auteurs/', blank=True) 
    telephone = models.CharField(max_length=20, blank=True) 
    ville = models.CharField(max_length=100, blank=True)
    pays = models.CharField(max_length=100, default='Guinée') 
    site_web = models.URLField(blank=True)
    twitter = models.CharField(max_length=100, blank=True) 
    linkedin = models.CharField(max_length=100, blank=True)
    
    # Statistiques
    articles_publies = models.PositiveIntegerField(default=0) 
    date_inscription = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Profil Auteur" 
        verbose_name_plural = "Profils Auteurs"
        
    def __str__(self):
        return f"Profil de {self.user.username}"

class Article(models.Model): 
    """Article de magazine"""
    
    # Informations de base
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contenu = models.TextField(blank=True)
    resume = models.TextField(max_length=300, blank=True)
    
    # RELATIONS ForeignKey
    auteur = models.ForeignKey( 
        Auteur,
        on_delete=models.CASCADE, # Si auteur supprimé → articles supprimés
        related_name='articles' # Accès inverse : auteur.articles.all() 
    )
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL, # Si catégorie supprimée → null null=True,
        null=True,
        blank=True,
        related_name='articles'
    )
    
    # RELATION ManyToMany 
    
    tags = models.ManyToManyField(
        Tag,
        related_name='articles',
        blank=True # Les tags sont optionnels
    )
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True) 
    date_publication = models.DateTimeField(null=True, blank=True) 
    publie = models.BooleanField(default=False)
    vues = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = "Article" 
        verbose_name_plural = "Articles" 
        ordering = ['-date_creation']
    def __str__(self): 
        return self.titre
