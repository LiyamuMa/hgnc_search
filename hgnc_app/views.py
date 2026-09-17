from django.shortcuts import render
from .modules.lightweight_dataset import search

def home(request):
    query = request.GET.get('search')
    gene = None
    invalid = False

    if query:
        cleaned_query = "".join(query.upper().split())
        if not cleaned_query.replace(":", "").isalnum():
            invalid = True
        else:
            gene = search(cleaned_query)

    return render(request, 'home.html', {'query': query, 'gene': gene, 'invalid': invalid})


