from django.contrib.auth import get_user_model
from django.db import models



class Request(models.Model):
    email = models.EmailField(verbose_name="Email")
    nickname = models.CharField(verbose_name='Ваш никнейм', max_length=50)
    volume = models.TextField(verbose_name='Объем товара', null=False, blank=False, max_length=1000)
    description = models.TextField(verbose_name='Описание', null=False, blank=False, max_length=1000)
    weight = models.IntegerField(verbose_name='Вес', null=True, blank=True)
    place = models.CharField(verbose_name="Местонахождение", max_length=500)
    send_date = models.DateTimeField(verbose_name='Дата отправки', null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='reviews',
                               verbose_name='Автор')



    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f'{self.tutor} {self.text} {self.author}'
