from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import render
from users.forms import ItensForm
from users.models import *

#mostrar todos os itens no index e quem postou
def IndexView(request):
    itens = ItensFeira.objects.all()

    return render(request, 'index.html', {'itens': itens})
