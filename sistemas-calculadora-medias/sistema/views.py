from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader


# request = requisição que é feita no navegador para o back-end
# response = resposta que o back-end devolve para o navegador
def index(request: HttpRequest) -> HttpResponse:
    # obteve o aqruivo templates/index.html e armazena na varaivel template
    template = loader.get_template(template_name="index.html")
    # Renderizar o template armazenado na variaevel html,ou seja,
    # vai gerar o html
    html = template.render(context={}, request=request)
    # instanciando um objeto da classe HttpResponse definindo o que será
    # retornado da requisição
    response = HttpResponse(content=html)

    return response


def contato(request: HttpRequest) -> HttpResponse:
    return render(request, "contato.html", context={})


def calculadora(request: HttpRequest) -> HttpResponse:
    return render(request, "calculadora.html", context={})


def calcular(request: HttpRequest) -> HttpResponse:
    # request.GET é o metodo da requisição, quais são as possiveis de utilizar:
    # request.GET a informação vai na url(https://localhost:8000/sistema/calcular?numero1=9&numero2=11)
    # request.GET a informação vai por de baixo dos panos(https://localhost:8000/sistema/calcular)
    # .get => é utilizado para obter um valor
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    soma = numero1 + numero2

    if numero1 > numero2:
        maior = "Primeiro número"
    else:
        maior = "Segundo número"

    dados_para_html = {
        "soma": soma,
        "maior": maior,
        "numero1": numero1,
        "numero2": numero2
    }

    return render(request, "resultado.html", context = dados_para_html)


def aluno(request: HttpRequest) -> HttpResponse:
    return render(request, "aluno.html", context={})

def calcular_media(request: HttpRequest) -> HttpResponse:
    media1 = float(request.GET.get("media1"))
    media2 = float(request.GET.get("media2"))
    media3 = float(request.GET.get("media3"))
    media_final = (media1 + media2 + media3) / 3

    if media_final >= 7:
        apr_rep = "Aluno aprovado"
    elif media_final >= 5 and media_final < 7:
        apr_rep = "Aluno em exame"
    else:
        apr_rep = "Aluno reprovado"

    aluno_dados = {
        "media1": media1,
        "media2": media2,
        "media3": media3,
        "media_final": media_final,
        "status": apr_rep
    }

    return render(request, "calcular_media.html", context=aluno_dados)