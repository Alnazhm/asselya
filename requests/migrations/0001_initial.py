# Generated by Django 4.1.7 on 2023-02-21 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('nickname', models.CharField(max_length=50, verbose_name='Как можем обратиться')),
                ('volume', models.TextField(max_length=1000, verbose_name='Объем товара')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Вес')),
                ('place', models.CharField(max_length=500, verbose_name='Местонахождение')),
                ('send_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
            },
        ),
    ]
