from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Room(models.Model):
    PUBLIC = 'pub'
    PRIVATE = 'pv'

    ROOM_TYPE = (
        (PUBLIC, 'Общая группа'),
        (PRIVATE, 'Приватная бесседа'),
    )

    type = models.CharField(max_length=3, choices=ROOM_TYPE, default=PRIVATE)
    name = models.CharField(max_length=64, unique=True)


    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name





class UserPage(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    foto = models.ImageField(upload_to="img/%Y/%m/%d/", null=True, blank=True)
    name = models.CharField(max_length=64)
    rooms = models.ManyToManyField(Room, blank=True, related_name='users')


    def __str__(self):
        return f'{self.name}'




class Message(models.Model):

    author = models.ForeignKey(UserPage, on_delete=models.CASCADE, related_name='author')
    content = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)
    room_from = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната', blank=True, null=True,
                                  related_name='messages')
    report = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    read_message = models.BooleanField(default=False)

    def __str__(self):
        return self.content
