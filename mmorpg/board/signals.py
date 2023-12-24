from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

from board.models import Comment, Post


@receiver(post_save, sender=Comment)
def comment_save_user(instance, sender, **kwargs):
    comment = sender.objects.get(id=instance.id)
    if comment.commentPost is not None:
        autor = comment.commentPost.author
        message = f"Вам пришел отклик от {comment.commentUser} на объявление {comment.commentPost}"
        email = EmailMessage('Отклик на объявление',
                             message,
                             to=[autor.email], )

        email.send()

    else:
        autor = comment.parent.commentUser
        message = f"Вам пришел отклик от {comment.commentUser} на объявление {comment.parent}"
        email = EmailMessage('Отклик на объявление',
                             message,
                             to=[autor.email], )

        email.send()


@receiver(post_save, sender=Post)
def save_news(instance, sender, **kwargs):
    post = sender.objects.get(id=instance.id)
    print(post.category)
    if post.category.id == 4:
        print(post.category)
        pipls = User.objects.all()
        message = f'Опубликована новость {post}!'
        for i in pipls:
            email = EmailMessage('Новость опубликована',
                             message,
                             to=[i.email], )

            email.send()
    print(post.category.id)