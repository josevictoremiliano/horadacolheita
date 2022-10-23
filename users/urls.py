from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import *

app_name = "users"

urlpatterns = [
    path("login", LoginPageView, name="login"),
    path("cadastro", CadastroPageView, name="cadastro"),
    path("recuperar", EsqueciSenhaView, name="recuperar-senha"),
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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)