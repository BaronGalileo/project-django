from django.contrib import admin
from .models import Category, Post

# напишем уже знакомую нам функцию обнуления товара на складе
def nullfy_quantity(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(text='')
nullfy_quantity.short_description = 'Удалить текст статьи' # описание для более понятного представления в админ панеле задаётся, как будто это объект


# создаём новый класс для представления товаров в админке
class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Product._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения
    list_display = ('author', 'title', 'categoryType', 'on_stock')
    list_filter = ('title', 'categoryType', 'author')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'text')  # тут всё очень похоже на фильтры из запросов в базу
    actions = [nullfy_quantity]  # добавляем действия в список

admin.site.register(Category)
admin.site.register(Post, ProductAdmin)
from django.contrib import admin

# Register your models here.
