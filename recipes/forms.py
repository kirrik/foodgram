from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'tag', 'cooking_time', 'text', 'image')

        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }
