from django import forms
from .models import Superhero


class superhero_forms(forms.ModelForm):
    class Meta:
        model = Superhero
        fields = '__all__'