from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path("login", LoginPageView, name="login"),
    path("cadastro", CadastroPageView, name="cadastro"),
    path("perfil/<pk>/recuperar", RecuperarPageView, name="recuperar-senha"),
    path('deslogar', logout),
    #perfil
    path('perfil', PerfilPageView.as_view(), name='perfil'),
    #editar foto ou excluir
    path('perfil/editar/<pk>', PerfilEditView, name='perfil-editar'),
    path('perfil/excluir/<pk>', PerfilDeleteView.as_view(), name='perfil-excluir'),
    #editar itens 
    path('perfil/editar-itens/<pk>', ItensEditView, name='itens-editar'),
    path('perfil/excluir-itens/<pk>', ItensDeleteView.as_view(), name='itens-excluir'),
    #Criar itens
    path('perfil/criar-itens', ItensCreateView, name='itens-criar'),

]