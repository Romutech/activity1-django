from django.db import models
from pprint import pprint

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=False)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

    # En cas de besoin, vous êtes autorisé à rajouter des méthodes ou
    # propriétés dans ce modèle.


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    pseudo      = models.CharField(max_length=50)
    mail        = models.EmailField(max_length=254) 
    content     = models.TextField(null=True)
    date        = models.DateTimeField(verbose_name="Date de publication", auto_now_add=True, auto_now=False)
    is_visible  = models.BooleanField(verbose_name="Le commentaire est visible ?", default=True)
    article     = models.ForeignKey('Article', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Commentaire"
        ordering = ['date']

    def __str__(self):
        return self.content
