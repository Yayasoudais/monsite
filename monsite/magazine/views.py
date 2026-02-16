from django.shortcuts import render, get_object_or_404 
from django.db.models import Q, F, Count
from .models import Article, Auteur, Categorie, Tag

def liste_articles(request):
    """Liste tous les articles publiés""" 
    articles = Article.objects.filter(
        publie=True 
    ).select_related(
        'auteur', 'categorie' 
    ).prefetch_related(
        'tags' 
    ).order_by('-date_publication')
    
    context = {
        'articles': articles, 
        'titre_page': 'Tous les articles'
    }
    return render(request, 'magazine/liste_articles.html', context)

def detail_article(request, slug): 
    """Détail d'un article""" 
    article = get_object_or_404(
        Article.objects.select_related('auteur', 'categorie').prefetch_related('tags'), 
        slug=slug,
        publie=True
    )
    
    # Incrémenter les vues
    Article.objects.filter(id=article.id).update(vues=F('vues') + 1)
    
    # Articles similaires (même catégorie)
    articles_similaires = Article.objects.filter( 
        categorie=article.categorie, 
        publie=True
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'articles_similaires': articles_similaires
    }
    return render(request, 'magazine/detail_article.html', context)

def articles_par_categorie(request, slug):
    """Articles d'une catégorie"""
    
    categorie = get_object_or_404(Categorie, slug=slug) 
    articles = Article.objects.filter(
        categorie=categorie,
        publie=True).select_related('auteur').prefetch_related('tags').order_by('-date_publication') 
    
    context = {
    'categorie': categorie,
    'articles': articles,
    'titre_page': f'Articles - {categorie.nom}'
    }
    return render(request, 'magazine/articles_categorie.html', context) 

def articles_par_auteur(request, id):
    """Articles d'un auteur"""
    
    auteur = get_object_or_404(Auteur, id=id) 
    articles = Article.objects.filter( 
        auteur=auteur,
        publie=True 
    ).select_related('categorie').prefetch_related('tags').order_by('-date_publication')

    # Stats de l'auteur
    stats = {
    'total_articles': articles.count(),
    'total_vues': sum(a.vues for a in articles), }

    context = {
        'auteur': auteur,
        'articles': articles,
        'stats': stats,
        'titre_page': f'Articles de {auteur.nom_complet}'
    }
    return render(request, 'magazine/articles_auteur.html', context)

def articles_par_tag(request, slug):
    """Articles avec un tag spécifique"""
    tag = get_object_or_404(Tag, slug=slug) 
    articles = Article.objects.filter( 
        tags=tag, 
        publie=True 
    ).select_related('auteur', 'categorie').prefetch_related('tags').order_by('-date_publication') 
    context = {
        'tag': tag,
        'articles': articles,
        'titre_page': f'Articles avec le tag #{tag.nom}'
    }
    return render(request, 'magazine/articles_tag.html', context)

def recherche(request): 
    """Recherche d'articles"""
    query = request.GET.get('q', '') 
    if query:
        articles = Article.objects.filter( 
            Q(titre__icontains=query) | Q(contenu__icontains=query) | 
            Q(resume__icontains=query),
            publie=True
        ).select_related('auteur', 'categorie').prefetch_related('tags')
    else:
        articles = Article.objects.none()
        
    context = {
        'query': query,
        'articles': articles, 
        'nombre_resultats': articles.count(), 
        'titre_page': f'Recherche : {query}'
    }
    return render(request, 'magazine/recherche.html', context)

def categories_liste(request):
    """Liste des catégories avec nombre d'articles"""
    categories = Categorie.objects.annotate( 
        nb_articles=Count('articles', filter=Q(articles__publie=True)) 
    ).filter(nb_articles__gt=0).order_by('-nb_articles')
    
    context = {
        'categories': categories,
        'titre_page': 'Toutes les catégories' 
    }
    return render(request, 'magazine/categories.html', context)

def auteurs_liste(request):
    """Liste des auteurs avec stats"""
    auteurs = Auteur.objects.annotate( 
        nb_articles=Count('articles', filter=Q(articles__publie=True)) 
    ).filter(nb_articles__gt=0).order_by('-nb_articles')

    context = {
        'auteurs': auteurs,
        'titre_page': 'Nos auteurs' 
    }
    return render(request, 'magazine/auteurs.html', context)

