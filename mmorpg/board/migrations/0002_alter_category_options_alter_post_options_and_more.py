# Generated by Django 5.0 on 2023-12-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_app']},
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='users',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
