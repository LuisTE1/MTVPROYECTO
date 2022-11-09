
from django.urls import path
from AppMTV.views import familiares, lista_familiares, family, lista_family,Formulario

urlpatterns = [
path('agregafamiliar/<celular>/<nombre>/<parentesco>', familiares),
    path('lista-familiares', lista_familiares),
    path('agregafamily/<fecha_nacimiento>/<celular>/<nombre>/<parentesco>', family),
    path('lista-family', lista_family),
    path('Formulario/', Formulario),
    ]