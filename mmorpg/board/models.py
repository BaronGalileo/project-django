from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, )

    EVERYONE = "EN"
    TANKS = "TT"
    HEALERS = "HIL"
    DAMAGE_DEALERS = "DD"
    TRADERS = "TD"
    QUILD_MASTERS = "GM"
    QUESTGIVERS = "QG"
    BLACKSMITHS = "BS"
    TANNERS = "TN"
    POTIONS_MAKERS = "PM"
    SPELL_MASTERS = "SM"
    CATEGORY_CHOICES = (
        (EVERYONE, 'Все жители'),
        (TANKS, 'Танки'),
        (HEALERS, 'Хилы'),
        (DAMAGE_DEALERS, 'Дамагеры'),
        (TRADERS, 'Торговцы'),
        (QUILD_MASTERS, 'Гильдмастеры'),
        (QUESTGIVERS, 'Квестгиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (TANNERS, 'Кожевники'),
        (POTIONS_MAKERS, 'Зельевары'),
        (SPELL_MASTERS, 'Мастера заклинаний'),
    )

    categoryType = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=EVERYONE)
    title = models.CharField(max_length=50, unique=True)
    content = CKEditor5Field(verbose_name='Сообщение')
    date_app = models.DateTimeField('Дата публикации', auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категории")


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/post/{self.id}'



    class Meta:
        ordering = ['-date_app']


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Комментарий', blank=True, null=True,
                                    related_name='commets')
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Комментатор")

    text = models.TextField(verbose_name='Текст')
    dateCreation = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-dateCreation']


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)





    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


    class Meta:
        ordering = ['id']
