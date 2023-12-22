from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import UpdateView
from prompt_toolkit.validation import ValidationError
from django.contrib.auth.tokens import default_token_generator as token_generator

from users.forms import LoginUserForm, ProfileUserForm, RegisterUserForm
from users.utils import send_mail_activ


class LoginUser(LoginView):
    model = User
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class RegisterUser(View):
    template_name = 'users/register.html'

    def get(self, request):
        context = {
            'form': RegisterUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            user.is_active = False
            user.save()
            send_mail_activ(request, user)

            return HttpResponse('Пожалуйста проверьте почту, чтобы завершить успешно регистрацию')
        else:
            form = RegisterUserForm()
        return render(request, 'users/register.html', {'form': form})


class RegisterEmail(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.is_active = True
            user.is_staff = True  # для загрузки фото в создании объявления
            user.save()
            return redirect('users:login')
        return HttpResponse('Ваша ссылка не корректна, повторите регистрацию ')

    @staticmethod
    def get_user(uidb64):

        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
