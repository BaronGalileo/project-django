from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserPage(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="img", null=True, blank=True)
    room = models.ManyToManyField('Room')
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.user_profile.username


class Room(models.Model):
    PUBLIC = 'pub'
    PRIVATE = 'pv'

    ROOM_TYPE = (
        (PUBLIC, 'Общая группа'),
        (PRIVATE, 'Приватная бесседа'),
    )

    type = models.CharField(max_length=3, choices=ROOM_TYPE, default=PRIVATE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)
    room_from = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната', blank=True, null=True,
                                  related_name='messages')
    report = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content
