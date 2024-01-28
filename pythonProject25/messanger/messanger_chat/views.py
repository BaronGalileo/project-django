from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import FormMixin

from .forms import *
from .models import UserPage, Room


# Create your views here.

@login_required
def index(request):

    content = {}
    return render(request, 'index.html', content)



class RoomList(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RoomDetail(FormMixin, DetailView):
    model = Room
    form_class = AddMessages
    template_name = 'room.html'
    context_object_name = 'chat'


    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.room_from = self.get_object()
            form.save()
            return redirect('room', pk=self.get_object().id)


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            # form.author = request.user
            form.save()

            return redirect('home')


        else:
            error = 'Форма была неверной'

    form = AddRoom()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'add_room.html', data)







