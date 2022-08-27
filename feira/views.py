from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import render
from users.models import *

def IndexPageView(request):
   
    return render(request, "index.html")

class IndexView(ListView):
    model = ItensFeira
    template_name = "index.html"
    paginate_by: int = 10
    page_kwarg: str = "feirantes"
