import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('genre/', mainapp.genre, name='genre'),
    path('genre/category/<int:category_pk>/', mainapp.genre_section, name='genre_section'),
    path('genre/game/<int:game_pk>/', mainapp.game_page, name='game_page'),

    path('genre/create/', mainapp.add_genre, name='add_genre'),
    path('genre/edit/<int:pk>/', mainapp.edit_genre, name='edit_genre'),
    path('genre/remove/<int:pk>/', mainapp.delete_genre, name='delete_genre'),

    path('genre/game/add/', mainapp.add_game, name='add_game'),
    path('genre/edit/game/<int:pk>/', mainapp.edit_game, name='edit_game'),
    path('genre/remove/game/<int:pk>/', mainapp.delete_game, name='delete_game'),
]
