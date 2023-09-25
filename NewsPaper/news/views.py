from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm
from .models import Post




class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def get_queryset(self):
    #
    #     queryset = super().get_queryset()
    #     self.filterset =PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['fresh_news'] = "Сегодня в 16.00 репортаж с места проишествия!"
        # context["news_list"] = Post.objects.all().order_by('-dateCreation')
        context['filterset'] = self.filterset
        return context

class MyViev(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):

        queryset = super().get_queryset()
        self.filterset =PostFilter(self.request.GET, queryset)
        return self.filterset.qs




    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        # context['fresh_news'] = "Сегодня в 16.00 репортаж с места проишествия!"
        # context["news_list"] = Post.objects.all().order_by('-dateCreation')
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['fresh_news'] = "Сегодня в 16.00 репортаж с места проишествия!"


        return context

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)








#
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')

class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_queryset(self):
        return Post.objects.filter(categoryType='AR')



class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


    def get_queryset(self):
        return Post.objects.filter(categoryType='NW')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(categoryType='AR')



