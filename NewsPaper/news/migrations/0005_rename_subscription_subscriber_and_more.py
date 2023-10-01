# Generated by Django 4.2.5 on 2023-10-01 16:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0004_category_subscribers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscription',
            new_name='Subscriber',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
    ]