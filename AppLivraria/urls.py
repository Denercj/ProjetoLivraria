from django.urls.conf import path
from AppLivraria.views import Index, CriaLivro, ListaLivro
from AppLivraria.models import Livro

urlpatterns = [
    path('',Index.as_view(),name="index"),
    path('livraria/cadastrar/', CriaLivro.as_view(model=Livro), name="cadastra_livro"),
    path('livraria/listar/', ListaLivro.as_view(), name="lista_livros"),
]