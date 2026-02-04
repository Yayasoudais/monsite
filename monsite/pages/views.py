from django.shortcuts import render

# Create your views here.
ARTICLES =[
    {   
        'id': 1,
        'titre': 'Introduction à Django',
        'contenu': 'Django est un framework web Python puissant et élégant',
        'auteur': 'Marie Dupont', 
        'date': '2026-01-01', 
        'tags': ['Django', 'Python', 'web'],
    } ,
    {
        'id': 2,
        'titre': 'Les Templates Django',
        'contenu': 'Les templates permettent de séparer la logique de la présentation',
        'auteur': 'Paul Martin', 
        'date': '2026-01-05', 
        'tags': ['Django', 'Templates', 'HTHL'],
    },
    {
        'id': 3,
        'titre': 'Déploiement Django', 
        'contenu': 'Déployer Django en production nécessite quelques configurations',
        'auteur': 'Sophie Lefebvre', 
        'date': '2026-01-07', 
        'tags': ['Django', 'Déploiement', 'Production'],
    },
]
#===================Blog============================
def blog_home (request): 
    """Liste tous les articles""" 
    context = {
        'articles': ARTICLES, 
        'titre_page': 'Mon BLog Django', 
        'nombre_articles': len(ARTICLES),
    }
    return render(request, 'pages/blog_home.html', context)

def blog_article(request, article_id): 
    """Affiche un article spécifique""" 
    article = next((a for a in ARTICLES if a['id'] == article_id), None)
    
    context = {
        'article': article, 
    }
    return render(request, 'pages/blog_article.html', context)
#===================================================
def home(request):
    """Page d'accueil avec templates"""
    context ={
        'titre': 'Bienvenue sur Mon site Django',
        'description': 'Apprenez Django pas à pas',
        'annee': 2026,
        'techonologies':['Python','Django','HTML','CSS','JavaScript'],
        'nombre_visiteurs': 1250,
    }
    return render(request,'pages/home.html',context)

def about(request):
    return render(request,'pages/about.html')
def contact(request):
    return render(request,'pages/contact.html')