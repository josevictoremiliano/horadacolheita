from django import forms
from .models import *

class FeirantesForm(forms.ModelForm):
    class Meta:
        model = Feirantes
        fields = '__all__'

class ItensForm(forms.ModelForm):
    class Meta:
        model = ItensFeira
        fields = '__all__'