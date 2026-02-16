from django.db.models import Q, Count, Avg, F 
from .models import Article, Auteur, Categorie, Tag

def articles_populaires(min_vues=50):
    """Articles avec plus de X vues"""
    return Article.objects.filter(vues__gte=min_vues).order_by('-vues')

def articles_recents(jours=7): 
    """Articles des X derniers jours""" 
    from datetime import timedelta 
    from django.utils import timezone
    
    date_limite = timezone.now() - timedelta(days=jours)
    return Article.objects.filter(date_creation__gte=date_limite)

def recherche_articles(query): 
    """Recherche dans titre OU contenu""" 
    return Article.objects.filter(
        Q(titre__icontains=query) | Q(contenu__icontains=query),
        publie=True )
    
def auteurs_actifs():
    """Auteurs avec au moins 1 article publié""" 
    return Auteur.objects.annotate(
        nb_articles_publies=Count('articles', filter=Q(articles__publie=True)) ).filter(nb_articles_publies__gt=0)
        
def categories_top():
    """Catégories triées par nombre d'articles""" 
    return Categorie.objects.annotate(
        nb_articles=Count('articles') ).order_by('-nb_articles')
    
def tags_populaires(top=10): 
    """Tags les plus utilisés""" 
    return Tag.objects.annotate(
        nb_articles=Count('articles') ).order_by('-nb_articles')[:top]
    
def articles_par_auteur(auteur_id):
    """Tous les articles d'un auteur avec stats"""
    return Article.objects.filter(auteur_id=auteur_id).aggregate(
total=Count('id'), total_vues=Sum('vues'), moyenne_vues=Avg('vues')
)