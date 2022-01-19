from django.http.request import HttpRequest

from django.shortcuts import render

from core.github.models import Linguagem as LinguagemModel
from core.github.models import Repositorio as RepositorioModel

from core.github.services import fetch_repositorios


def index(request: HttpRequest):
    context = {
        "repositorios": [],
        "linguagens": []
    }

    linguagens = LinguagemModel.objects.all()

    if request.method == "POST":
        repositorios = RepositorioModel.objects.all()

        if repositorios.count() == 0:
            repositorios = fetch_repositorios()

            repositorios = (
                RepositorioModel(**repositorio)
                for repositorio in repositorios
            )

            repositorios = RepositorioModel.objects.bulk_create(repositorios)
        
        context["repositorios"] = repositorios
        
    context["linguagens"] = linguagens

    template_name = "index.html"
    
    return render(request, template_name, context)