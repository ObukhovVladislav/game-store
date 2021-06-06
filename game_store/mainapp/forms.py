from django import forms

from mainapp.models import GameCategory, Game


class CategoryForm(forms.ModelForm):
    class Meta:
        model = GameCategory
        fields = (
            'name',
            'desc',
        )


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = (
            'category',
            'name',
            'desc',
            'price',
        )


class DeleteGenre(forms.ModelForm):
    class Meta:
        model = GameCategory
        fields = (
            'name',
            'desc',
        )
