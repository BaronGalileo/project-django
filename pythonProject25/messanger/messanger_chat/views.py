from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import  ListView, FormView
from django.views.generic.edit import  CreateView, UpdateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from .forms import *
from .serializers import *


# Create your views here.

@login_required
def test(request):
    content = {}
    return render(request, 'test.html', content)


class ProfileList(ListView):
    """Домашняя"""
    model = UserPage
    template_name = 'rooms.html'
    context_object_name = 'profile'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_required
def create(request):
    error = ''
    name = request.POST.get("name", None)
    if request.method == 'POST':
        form = AddRoom(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()

            return HttpResponseRedirect(reverse("room", kwargs={"pk": Room.objects.get(name=name).pk}))

        elif Room.objects.get(name=name):
            return HttpResponseRedirect(reverse("room", kwargs={"pk": Room.objects.get(name=name).pk}))

        else:
            print(name)
            error = 'Форма была неверной'

    form = AddRoom()

    data = {
        'form': form,
        'error': error
    }
    print(error)
    return render(request, 'add_room.html', data)


class AccauntDetail(UpdateView):
    model = UserPage
    template_name = 'profile.html'
    context_object_name = 'profile'
    form_class = AddUserPage
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


"""----api----"""


class RoomAPIList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileAPIList(generics.ListCreateAPIView):
    queryset = UserPage.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPage.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)




def room(request, pk):


    room: Room = get_object_or_404(Room, pk=pk)
    chat = room.messages
    profiles = UserPage.objects.all()
    data = {
        "room": room,
        'chat': chat,
        'user': profiles
    }
    print(data)
    return render(request, 'room_api.html', data)
