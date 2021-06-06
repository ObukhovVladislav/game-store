from django.contrib.auth.models import User
from django.db import models


class GameCategory(models.Model):
    name = models.CharField('Название', max_length=60)
    desc = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория игр'
        verbose_name_plural = 'Категории игр'


class Game(models.Model):
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=60)
    desc = models.TextField('Описание', blank=True)
    price = models.CharField('Цена', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
