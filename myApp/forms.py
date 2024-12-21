from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for items in choices:
    choice_list.append(items)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',) #Only passing body so that the comment doesn't show option to change name!!!
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }