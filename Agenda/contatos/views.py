from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html',{ 'contatos': contatos
    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    #if not contato.mostrar:
    #    raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

