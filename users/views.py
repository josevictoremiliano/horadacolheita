from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from users.forms import FeirantesForm

from users.models import *


# Create your views here.
def LoginPageView(request):
    template_name = "users/login.html"
    
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('/')

    return render(request, template_name, {})

class tLoginPageView(LoginRequiredMixin, ListView):
    model = Feirantes
    template_name = 'users/login.html'
    context_object_name = 'Feirantes'
    login_url = 'login'

    def get_queryset(self):
        return Feirantes.objects.filter(user=self.request.user)

class CadastroPageView(CreateView):
    model = Feirantes
    template_name = 'users/cadastro.html'
    form_class = FeirantesForm
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def RecuperarPageView(request):
    return render(request, "users/recuperar.html")

def sair(request):
    logout(request)
    return HttpResponseRedirect('/')