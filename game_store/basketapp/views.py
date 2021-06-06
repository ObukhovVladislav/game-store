from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from basketapp.models import GameBasket
from mainapp.models import Game


def index(request):
    item = GameBasket.objects.filter(user=request.user)
    context = {
        'object_list': item,
    }
    return render(request, 'basketapp/basket.html', context)


def add(request, game_id):
    game = Game.objects.get(pk=game_id)
    GameBasket.objects.get_or_create(
        user=request.user,
        game=game
    )
    return HttpResponseRedirect(
        reverse('mainapp:catalog_section',
                kwargs={'category_pk': game.category_id})
    )


def remove(request, game_basket_id):
    item = GameBasket.objects.get(id=game_basket_id)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
