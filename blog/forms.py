from .models import Comment, CollaborateRequest
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CollaborateForm
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')        