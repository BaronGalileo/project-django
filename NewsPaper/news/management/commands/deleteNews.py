from django.core.management.base import BaseCommand, CommandError
from news.models import Post


class Command(BaseCommand):
    help = 'Подсказка вашей команды'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполнется при вызове вашей команды
        self.stdout.readable()
        self.stdout.write(
            'Do you really want to delete all posts? select a category: Политика/Экономика/Искусство/Наука')  # спрашиваем пользователя действительно ли он хочет удалить все товары
        answer = input()  # считываем подтверждение




        if answer == 'Политика':  # в случае подтверждения действительно удаляем все товары
            Post.objects.filter(postCategory__name='Политика').delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped posts "Политика"!'))
            return

        if answer == 'Экономика':  # в случае подтверждения действительно удаляем все товары
            Post.objects.filter(postCategory__name='Экономика').delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped posts "Экономика"!'))
            return

        if answer == 'Искусство':  # в случае подтверждения действительно удаляем все товары
            Post.objects.filter(postCategory__name='Искусство').delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped posts "Искусство"!'))
            return

        if answer == 'Наука':  # в случае подтверждения действительно удаляем все товары
            Post.objects.filter(postCategory__name='Наука').delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped posts "Наука"!'))
            return

        self.stdout.write(
            self.style.ERROR('Access denied'))  # в случае неправильного подтверждения, говорим что в доступе отказано