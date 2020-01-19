from django import forms
from .models import Comment

class CommentForm(forms.Form):
   pseudo =		forms.CharField(max_length=50, label="Pseudo")
   mail = 		forms.EmailField(max_length=254, label="Email") 
   content = 	forms.CharField(widget=forms.Textarea, label="Contenu")
