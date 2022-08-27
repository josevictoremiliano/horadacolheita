from django import forms
from .models import *

class FeiratesForm(forms.ModelForm):
    class Meta:
        model = Feirates
        fields = '__all__'

class ItensForm(forms.ModelForm):
    class Meta:
        model = Itens
        fields = '__all__'