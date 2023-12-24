from django_ckeditor_5.widgets import *
from django.forms import TextInput

from .models import Post, Comment



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




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ComForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commentPost', 'commentUser', 'text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if self.fields[field] == self.fields['parent']:
                print('parent')
            else:
                self.fields[field].widget.attrs['class'] = 'form-control'





