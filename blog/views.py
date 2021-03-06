from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm


def accueil(request):
    """
    Affiche les 5 derniers articles du blog. Nous n'avons pas encore
    vu comment faire de la pagination, donc on ne donne pas la
    possibilité de lire les articles plus vieux via l'accueil pour
    le moment.
    """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:4]

    return render(request, 'blog/accueil.html', {'articles': articles})


def lire_article(request, slug):
    """
    Affiche un article complet, sélectionné en fonction du slug
    fourni en paramètre
    """
    article    = get_object_or_404(Article, slug=slug)
    comments    = Comment.objects.filter(is_visible=True, article=article).order_by('-date')[:4]   
    form        = CommentForm(request.POST or None)

    if form.is_valid():
        comment             = Comment()
        comment.pseudo      = form.cleaned_data['pseudo']
        comment.mail        = form.cleaned_data['mail']
        comment.content     = form.cleaned_data['content']
        comment.article     = article
        comment.save()
        return redirect('/blog/' + slug)

    return render(request, 'blog/lire_article.html', locals())

