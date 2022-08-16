from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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

def CadastroPageView(request):
    return render(request, "users/cadastro.html")

def RecuperarPageView(request):
    return render(request, "users/recuperar.html")

def sair(request):
    logout(request)
    return HttpResponseRedirect('/')