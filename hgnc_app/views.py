from django.shortcuts import render
from .modules.lightweight_dataset import search

def home(request):

    """
    Display the home page and handle gene searches.

    Retrieves a gene ID or symbol from the search query, validates the
    input to only allow alphanumeric symbols and semi-colons, and searches
    the HGNC dataset for a matching gene. The search results and validation
    status are passed to the home page template.
    """

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


