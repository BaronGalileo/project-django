from django import forms
from django.core.exceptions import ValidationError
from django.views.generic import CreateView

from .models import *


class PostForm(forms.ModelForm):



    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'postCategory',
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