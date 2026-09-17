from ..views import home
from django.test import RequestFactory

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")

import django
django.setup()


def test_home_no_search():
    request = RequestFactory().get("/")
    response = home(request)
    assert response.status_code == 200

def test_home_invalid(client):
    response = client.get("/", {"search": "A!BG"})

    assert response.status_code == 200
    assert response.context["invalid"] is True

def test_home_valid(client):
    response = client.get("/", {"search": "A1BG"})

    assert response.status_code == 200
    assert response.context["gene"]["gene_symbol"] == "A1BG"
    assert response.context["gene"]["hgnc_id"] == "HGNC:5"
    assert response.context["gene"]["gene_name"] == "alpha-1-B glycoprotein"
    assert response.context["gene"]["previous_gene_symbol"] == []
    assert response.context["gene"]["previous_gene_name"] == []
    assert response.context["gene"]["alias_symbol"] == []
    assert response.context["gene"]["alias_name"] == []
    assert response.context["gene"]["mane_select_transcripts"] == ["ENST00000263100.8", "NM_130786.4"]
