from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from datetime import datetime

from django.views.generic.edit import FormMixin

from .forms import PostForm, CommentForm
from .models import Post, Category, Comment


def index(request):
    return render(request, 'board/index.html')


def cat(request):
    return render(request, 'board/cat.html')


def message(request):
    return render(request, 'board/message.html')


class MyPostList(ListView):
    model = Post
    template_name = 'board/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_app']
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


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



class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.commentPost = self.get_object()
            form.commentUser = request.user
            form.save()
            return redirect('post', pk=self.get_object().id)


class CommentDelete(DeleteView):
    model = Comment
    template_name = 'board/comment_delete.html'
    context_object_name = 'comment'
    success_url = '/messages'


class CommentResponse(FormMixin, DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'board/comment-response.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id =int(request.POST.get('parent'))
            form.commentUser = request.user
            form.save()

            return redirect('/messages')



class PostUpdateDetail(UpdateView):
    model = Post
    template_name = 'board/create.html'
    form_class = PostForm


class PostDeleteDetail(DeleteView):
    model = Post
    template_name = 'board/post_delete.html'
    success_url = 'home'
    form_class = PostForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fresh_news'] = "Сегодня в 16.00 стрим от Gringo!"
        context['time_now'] = datetime.now()
        return context


class CommentList(ListView):

    model = Comment
    template_name = 'board/comments.html'
    context_object_name = 'comments'
    paginate_by = 10


class CommentDetail(DetailView):
    model = Post
    template_name = 'board/post.html'
    context_object_name = 'post'
    form_class = CommentForm

    # def post(self, request, *args, **kwargs):
    #     if form.is_valid():
    #         form = form.save(commit=False)
    #         form.commentPost = self.get_object()
    #         form.commentUser = request.user
    #         form.save()
    #         return redirect('post', pk=self.get_object().id)
