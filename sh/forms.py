from .models import Shortner
from django.forms import ModelForm, TextInput


class ShortnerForm(ModelForm):
    class Meta:
        model = Shortner
        fields = ('urlOriginal',)
        widgets = {
            'urlOriginal': TextInput(attrs={'placeholder': 'Input URL'}),
        }
