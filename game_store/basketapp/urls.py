import basketapp.views as basketapp
from django.urls import path, include

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add/<int:game_id>/', basketapp.add, name='add'),
    path('remove/<int:game_basket_id>/', basketapp.remove, name='remove'),
]
