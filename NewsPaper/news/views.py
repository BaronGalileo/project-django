from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.



class PostList(ListView):
    model = Post



    template_name = 'posts.html'
    context_object_name = 'posts'




    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['fresh_news'] = "Сегодня в 16.00 репортаж с места проишествия!"
        context["news_list"] = Post.objects.all().order_by('-dateCreation')
        return context

class PostDetail(DetailView):
    model = Post

    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['fresh_news'] = "Сегодня в 16.00 репортаж с места проишествия!"


        return context