from django.urls import path 
from . import views

app_name = 'magazine'

urlpatterns = [
path('', views.liste_articles, name='liste_articles'),
path('article/<slug:slug>/', views.detail_article, name='detail_article'),
path('categorie/<slug:slug>/', views.articles_par_categorie, name='articles_categorie'), 
path('auteur/<int:id>/', views.articles_par_auteur, name='articles_auteur'), 
path('tag/<slug:slug>/', views.articles_par_tag, name='articles_tag'), 
path('recherche/', views.recherche, name='recherche'),
path('categories/', views.categories_liste, name='categories'),
path('auteurs/', views.auteurs_liste, name='auteurs'), 
]