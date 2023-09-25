from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm
from .models import Post




class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):

        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset =PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs




    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
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
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset =PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs




    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow()
        # context['fresh_news'] = "Сегодня в 16.00 репортаж с места проишествия!"
        # context["news_list"] = Post.objects.all().order_by('-dateCreation')
        context['filterset'] = self.filterset
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

class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post

    # и новый шаблон, в котором используется форма.
    template_name = 'post_edit.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)



#
# class ProductUpdate(UpdateView):
#     form_class = PostForm
#     model = Post
#     template_name = 'post_edit.html'
#
# class ProductDelete(DeleteView):
#     model = Post
#     template_name = 'post_delete.html'
#     success_url = reverse_lazy('post_list')
def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request,'post_search.html',)

def create_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/news/')


    return render(request, 'post_edit.html', {'form':form})
