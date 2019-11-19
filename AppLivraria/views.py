from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from AppLivraria.models import Livro
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView


class Index(TemplateView):
    template_name = "index.html"
    
class CriaLivro(CreateView):
    template_name = "cadastra.html"
    model = Livro()
    # na linha abaixo, será criado um campo para todos o atributos da classe criaLivro
    fields = '__all__'
    #aqui faz o caminho que seguirá quando clicar para criar o livro
    success_url = reverse_lazy("lista_livros")

class ListaLivro(ListView):
    template_name = "lista.html"
    model = Livro
    context_object_name = "livros"
    