from django import forms
from .models import Post, Parts
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('cloth_name', 'date_purchase', 'season',
                  'part', 'price',  'image')
        widgets = {
            'date_purchase': forms.SelectDateWidget
        }


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class PartsForm(forms.ModelForm):
    class Meta():
        model = Parts
        fields = ('name',)


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
