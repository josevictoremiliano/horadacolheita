from django.urls import path

from .views import *

app_name = "users"

urlpatterns = [
    path("login", LoginPageView, name="login"),
    path("cadastro", CadastroPageView.as_view(), name="cadastro"),
    path("recuperar", RecuperarPageView, name="recuperar-senha"),
    path('deslogar', sair),
]