import datetime

from celery import shared_task
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Category, Post
from django.conf import settings


@shared_task
def send_email(pk, to_email):

    preview = Post.objects.get(pk=pk).preview
    title = Post.objects.get(pk=pk).title
    html_content = render_to_string(
        'post_created_email.html',

        {
            'text': preview,

            'link': f'{settings.SITE_URL}/home/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=to_email,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.encoding = 'utf-8'
    msg.send()


@shared_task
def my_task():

    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__name', flat=True))
    subscriptions = set(
        Category.objects.filter(name__in=categories).values_list('subscriptions__user__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscriptions
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()