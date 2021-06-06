from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Game


class GameBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}: {self.game.name}'

    def to_html(self):
        return f'{self.added.strftime("%Y.%m.%d %H:%M")}: <b>{self.game.name}</b>'
