from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Message, Room, UserPage


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']


class AddMessages(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Сообщение', 'id': 'cont'})


class AddRoom(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название'})
        self.fields['type'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название'})

    class Meta:
        model = Room
        fields = ('name', 'type',)


class AddUserPage(forms.ModelForm):
    class Meta:
        model = UserPage
        fields = ('foto', 'name',)


class UpdateUserPage(forms.ModelForm):
    class Meta:
        model = UserPage
        fields = ('foto', 'name',)
