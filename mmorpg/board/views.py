from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from datetime import datetime

from .filters import PostFilter
from .forms import PostForm, CommentForm
from .models import Post, Category



def index(request):
    return render(request, 'board/index.html')


def cat(request):
    return render(request, 'board/cat.html')


def message(request):
    return render(request, 'board/message.html')



@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()

            return redirect('home')


        else:
            error = 'Форма была неверной'

    form = PostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'board/create.html', data)


@login_required
def CommentCreate(request, pk):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()

            return redirect('board/post/pk')
        else:
            error = 'Форма была неверной'

    form = PostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'board/post/pk.html', data)


class PostList(ListView):

    model = Post
    template_name = 'board/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_app']
    paginate_by = 3


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fresh_news'] = "Сегодня в 16.00 стрим от Gringo!"
        context['time_now'] = datetime.now()
        return context

class CategoryList(ListView):

    model = Category
    template_name = 'board/category.html'
    context_object_name = 'cat'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fresh_news'] = "Сегодня в 16.00 стрим от Gringo!"
        context['time_now'] = datetime.now()
        return context



