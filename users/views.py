from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout as auth_login
from django.contrib.auth.models import Group


from users.forms import ItensForm, ItensFormExtends, UserForm

from users.models import *


# Create your views here.
def LoginPageView(request):
    template_name = "users/login.html"
    data = {}
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            data['msg'] = 'Usuário ou senha inválidos!'
            data['class'] = 'alert-danger'

    return render(request, template_name, data)
    

def CadastroPageView(request):
    data = {}
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')

    
    if request.method == 'POST':
        print (request.POST)
        user = User.objects.create_user(
           #mandar os dados do form
            username=request.POST['csrfmiddlewaretoken'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            city=request.POST['city'],
           )
        user.username = request.POST['email']
        group = Group.objects.get(name='feirantes')
        user.groups.add(group)
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
        return redirect('/')
    else:
        print (request.POST)

    return render(request, 'users/cadastro.html', data)

def RecuperarPageView(request, pk):
    #trocar a senha
    user = User.objects.get(pk=pk, email=request.user.email)
    user.set_password(request.POST['trocasenha'])
    user.save()
    logout(request)
    redirect('/')
   
    return render(request, "users/recuperar.html")

def logout(request):
    auth_login(request)
    return redirect('/')


#perfil e visualizar itens
class PerfilPageView(ListView):
    model = User
    template_name = 'users/perfil.html'

    

    #get itens do usuario logado
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itens'] = ItensFeira.objects.filter(feirante=self.request.user.id)
        return context

 
   

    #editar foto ou excluir
    def get_ordering (self):
        return ['id']

#editar perfil enviar fotos e dados
def PerfilEditView(request, pk):
    template_name = 'users/perfil-editar.html'
    data = {}
    user = User.objects.get(pk=pk)
    form = UserForm(request.POST or None, request.FILES or None, instance=user)
    data['user'] = user
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users:perfil')
        else:
            data['form'] = form
            print(form.errors)
    return render(request, template_name, data)


class PerfilDeleteView(DeleteView):
    model = User
    template_name = 'users/perfil-excluir.html'
    success_url = reverse_lazy('users:perfil')

#editar itens

def ItensEditView(request, pk):
    template_name = 'users/itens-editar.html'
    data = {}
    itens = ItensFeira.objects.get(pk=pk)
    form = ItensForm(request.POST or None, instance=itens)
    data['itens'] = itens
    data['form'] = form
    current_user = request.user
    if request.method == 'POST':
        #setar o usuario logado como dono do item
        itens.id_feirante = current_user
        if form.is_valid():
            itens.save()
            form.save()
            return redirect('users:perfil')
        else:
            data['form'] = form
            print(form.errors)
    return render(request, template_name, data)

class ItensDeleteView(DeleteView):
    model = ItensFeira
    template_name = 'users/itens-excluir.html'
    success_url = reverse_lazy('users:perfil')

#criar itens
def ItensCreateView(request):
    template_name = 'users/itens-criar.html'
    data = {}

    if request.method == 'POST':
        form = ItensFormExtends(
            request.POST, 
            request.FILES)
        current_user = User.objects.get(email=request.user.email)
        #setar o usuario logado como dono do item
        form.instance.id_feirante = current_user
        if form.is_valid():
            
            form.save()
            return redirect('users:perfil')
        else:
            data['form'] = form
            print(form.errors)
    else:
        form = ItensFormExtends()
        data['form'] = form
    return render(request, template_name, data)
    