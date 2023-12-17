from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_ckeditor_5.widgets import *

from .models import Post
from django.forms import ModelForm, TextInput, SelectMultiple


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название', 'autocomplete': 'off'})
        self.fields['categoryType'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название', 'autocomplete': 'off'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Категория', 'autocomplete': 'off'})
        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5', 'placeholder': 'Объявление'})
        self.fields['content'].required = False



    class Meta:
        model = Post
        fields = ['title',  'category', 'categoryType', 'content']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }




