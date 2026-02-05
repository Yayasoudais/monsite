from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_home, name='blog_home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/<int:article_id>', views.blog_article, name='blog_article'),
#    path('services/',views.services, name='services'),
#   path('portfolio/', views.portfolio, name = 'portfolio'),
  
]