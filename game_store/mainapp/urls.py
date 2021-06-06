import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('genre/', mainapp.genre, name='genre'),

    path('genre/create/', mainapp.add_category, name='add_category'),
    path('genre/category/add/', mainapp.add_game, name='add_game'),

    path('genre/category/<int:category_pk>/', mainapp.genre_section, name='genre_section'),
    path('genre/game/<int:game_pk>/', mainapp.game_page, name='game_page'),
]
