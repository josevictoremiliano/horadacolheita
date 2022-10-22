from django import forms
from .models import *


class ItensForm(forms.ModelForm):
    class Meta:
        model = ItensFeira
        fields = ['name', 'description', 'price', 'image']
class ItensFormExtends(forms.ModelForm):
    class Meta:
        model = ItensFeira
        fields = '__all__'
        
        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserFormEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'city', 'avatar']