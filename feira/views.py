from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import render
from users.forms import ItensForm
from users.models import *

def IndexPageView(request):
   
    return render(request, "index.html")

def IndexView(request):
    itens = ItensFeira.objects.all()
    context = {
        'itens' : itens
    }
    return render(request, 'index.html', context)
