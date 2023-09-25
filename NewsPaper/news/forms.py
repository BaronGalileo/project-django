from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import CreateView

from .models import Post, Author


class PostForm(forms.ModelForm):

    title = forms.CharField(min_length=5)
    authors = Author.objects.all()
    author_list = [(i.authorUser.username,i.authorUser.username) for i in authors]
    author = forms.ChoiceField(choices=author_list)


    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'categoryType'
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data

    # def clean_name(self):
    #     title = self.cleaned_data["title"]
    #     if title[0].islower():
    #         raise ValidationError(
    #             "Название должно начинаться с заглавной буквы."
    #         )
    #     return title