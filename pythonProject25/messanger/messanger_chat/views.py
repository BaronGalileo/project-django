from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.edit import FormMixin, CreateView, UpdateView

from .forms import *
from .models import UserPage, Room


# Create your views here.

@login_required
def index(request):
    content = {}
    return render(request, 'index.html', content)


class ProfileList(ListView):
    """Домашняя"""
    model = UserPage
    template_name = 'rooms.html'
    context_object_name = 'profile'

    # def get_queryset(self):
    #     return super().get_queryset().filter(room.userpage=self.request.user)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RoomDetail(FormMixin, DetailView):
    """Сообщения в комнате"""

    model = Room
    form_class = AddMessages
    template_name = 'room.html'
    context_object_name = 'chat'

    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        context['profiles'] = UserPage.objects.all()
        context['user_name'] = Message.objects.values('author')
        return context

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.author_id = request.user.id
            form.room_from = self.get_object()
            if request.POST.get('report', None):
                form.report_id = int(request.POST.get('report'))
            form.save()
            return redirect('room', pk=self.get_object().id)


@login_required
def create(request):
    error = ''
    user = UserPage.objects.get(user_profile_id=request.user.id)
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            user.rooms.add(form)
            user.save()

            return redirect('room', pk=user.rooms.get(name=form).id)


        else:

            error = 'Форма была неверной'

    form = AddRoom()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'add_room.html', data)


@login_required
def selectRoom(request):
    error = ''
    user = UserPage.objects.get(user_profile_id=request.user.id)

    if request.method == 'POST':
        form = GetRoom(request.POST)
        room = Room.objects.all()
        name_room = request.POST.get('name')

        if Room.objects.filter(name__iexact=name_room):
            room_select = room.get(name=request.POST.get('name'))
            users_rooms = UserPage.objects.filter(rooms__name=room_select)
            if 'pv' == room_select.type and len(users_rooms) < 2:
                user.rooms.add(room_select)
                user.save()
                return redirect('room', pk=user.rooms.get(name=room_select).id)

            elif 'pub' == room_select.type:
                user.rooms.add(room_select)
                user.save()
                return redirect('room', pk=user.rooms.get(name=room_select).id)



            else:
                return redirect('add_room')





        else:

            error = 'Форма была неверной'

    form = GetRoom()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'get_room.html', data)


class AccauntDetail(UpdateView):
    model = UserPage
    template_name = 'profile.html'
    context_object_name = 'profile'
    form_class = UpdateUserPage
    success_url = '/'


class AccauntCreate(CreateView):
    model = UserPage
    template_name = 'addprofile.html'
    context_object_name = 'profile'
    form_class = AddUserPage
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.user_profile = request.user
            form.save()
            return redirect('home')

# class AddMessage(View):
#     """Сообщения"""
#
#     def post(self,request, pk):
#         form = AddMessages(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.room_from_id = pk
#             form.author = request.user
#             form.save()
#         return redirect('room', pk=pk)
