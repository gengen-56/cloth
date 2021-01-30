from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('cloth_name', 'date_purchase', 'season', 'part', 'image')
        widgets = {
            'date_purchase': forms.SelectDateWidget
        }
