from django.views.generic import TemplateView, ListView, DetailView

from django.shortcuts import render

def IndexPageView(request):
   
    return render(request, "index.html")
