from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver


from board.models import Comment


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


