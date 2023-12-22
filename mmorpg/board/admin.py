from django.contrib import admin
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Category, Post, Comment


class PostForm(forms.ModelForm):
    """Форма для редактора текста"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    content = forms.CharField(widget=CKEditor5Widget, label='Контент')

    class Meta:
        model = Post
        fields = "__all__"
        

class PostAdmin(admin.ModelAdmin):
    form = PostForm




admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
