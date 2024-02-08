from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    users = models.ManyToManyField('UserPage', blank=True, related_name='current_rooms')
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rooms")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class UserPage(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    foto = models.ImageField(upload_to="img/%Y/%m/%d/", null=True, blank=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    author = models.ForeignKey(UserPage, on_delete=models.CASCADE, related_name='author')
    content = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)
    room_from = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната', blank=True, null=True,
                                  related_name='messages')


    def __str__(self):
        return f"Message({self.author} {self.room_from})"
