# Generated by Django 4.2.5 on 2024-01-28 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messanger_chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='messanger_chat.room', verbose_name='Комната'),
        ),
    ]
