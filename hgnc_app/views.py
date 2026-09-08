from django.shortcuts import render
from .modules.lightweight_dataset import search

def home(request):
    query = request.GET.get('search')

    if query:
        gene = search("".join(query.upper().split()))
    else:
        gene = None

    return render(request, 'home.html', {'query': query, 'gene': gene})


