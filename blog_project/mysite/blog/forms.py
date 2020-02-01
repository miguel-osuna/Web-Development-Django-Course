from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    ''' Form definition for Post '''

    class Meta:
        ''' Meta definition for Postform '''
        model = Post
        fields = ("author", "title", "text")

    # Widgets are for custom styling the forms
    widgets = {
        "title": forms.TextInput(attrs={"class": "textinputclass"}),
        "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"})
    }


class CommentForm(forms.ModelForm):
    ''' Form definition for Comment '''

    class Meta:
        ''' Meta definition for Comment form '''
        model = Comment
        fields = ("author", "text")

    # Widgets are for custom styling the forms
    widgets = {
        "author": forms.TextInput(attrs={"class": "textinputclass"}),
        "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"})
    }
