from django.urls import include, path
from blog import views

urlpatterns = [
    path('accueil/', views.accueil, name='accueil'),
    path('<slug>', views.lire_article, name='blog_lire'),
    path('store/comment', views.store_comment, name='store_comment')
]
