from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound

from mainapp.forms import CategoryForm, GameForm, DeleteGenre
from mainapp.models import GameCategory, Game


@login_required()
def index(request):
    context = {
        'page_title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)


def genre(request):
    categories = GameCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'mainapp/genre.html', context)


def genre_section(request, category_pk):
    items = Game.objects.filter(category_id=category_pk)
    context = {
        'items': items,
        'page_title': 'страница игр'
    }
    return render(request, 'mainapp/genre_section.html', context)


def game_page(request, game_pk):
    game = Game.objects.get(pk=game_pk)
    context = {
        'game': game,
        'page_title': 'страница игры'
    }
    return render(request, 'mainapp/game_page.html', context)


def add_genre(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:genre'))
    else:
        form = CategoryForm()
    context = {
        'title': 'Добавить категорию',
        'form': form,
    }
    return render(request, 'mainapp/add_genre.html', context)


def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mainapp:genre'))
    else:
        form = GameForm()
    context = {
        'title': 'Добавить игру',
        'form': form,
    }
    return render(request, 'mainapp/add_game.html', context)


# def delete_genre(request, genre_id):
#     genre_delete = get_object_or_404(CategoryForm, id=genre_id)
#     if request.method == 'POST':
#         form = DeleteGenre(request.POST, instance=genre_delete)
#         if form.is_valid():
#             genre_delete.delete()
#             return HttpResponseRedirect(reverse('mainapp:genre'))
#     else:
#         form = DeleteGenre(instance=genre_delete)
#     template_vars = {'form': form}
#     return render(request, 'mainapp/delete_genre.html', template_vars)
