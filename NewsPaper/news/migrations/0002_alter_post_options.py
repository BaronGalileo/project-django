# Generated by Django 4.2.5 on 2023-09-24 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-dateCreation', 'title']},
        ),
    ]