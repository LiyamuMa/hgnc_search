from ..modules.lightweight_dataset import search, extract_lite, clean

#Testing search() with different inputs
def test_search_by_symbol():
    result = search("A1BG")
    assert result["gene_symbol"] == "A1BG"
    assert result["hgnc_id"] == "HGNC:5"
    assert result["gene_name"] == "alpha-1-B glycoprotein"
    assert result["previous_gene_symbol"] == []
    assert result["previous_gene_name"] == []
    assert result["alias_symbol"] == []
    assert result["alias_name"] == []
    assert result["mane_select_transcripts"] == ["ENST00000263100.8", "NM_130786.4"]

def test_search_by_id():
    result = search("HGNC:30005")
    assert result["gene_symbol"] == "A3GALT2"
    assert result["hgnc_id"] == "HGNC:30005"
    assert result["gene_name"] == "alpha 1,3-galactosyltransferase 2"
    assert result["previous_gene_symbol"] == ["A3GALT2P"]
    assert result["previous_gene_name"] == ["alpha 1,3-galactosyltransferase 2, pseudogene"]
    assert result["alias_symbol"] == ["IGBS3S", "IGB3S"]
    assert result ["alias_name"] == ["iGb3 synthase", "isoglobotriaosylceramide synthase"]
    assert result["mane_select_transcripts"] == ["ENST00000442999.3", "NM_001080438.1"]

def test_search_by_number():
    result = search("60")
    assert result["gene_symbol"] == "ABCC9"
    assert result["hgnc_id"] == "HGNC:60"
    assert result["gene_name"] == "ATP binding cassette subfamily C member 9"
    assert result["previous_gene_symbol"] == []
    assert result["previous_gene_name"] == ["ATP-binding cassette, sub-family C (CFTR/MRP), member 9"]
    assert result["alias_symbol"] == ["SUR2", "CMD1O"]
    assert result ["alias_name"] == ["sulfonylurea receptor 2"]
    assert result["mane_select_transcripts"] == ["ENST00000261200.9", "NM_020297.4"]

def test_search_no_value():
    result = search("NOTAGENE1")
    assert result is None


#testing extract_lite() with test_row that has extra columns
def test_extract_lite():
    test_row = {
        "hgnc_id": "HGNC:5",
        "symbol": "A1BG",
        "name": "alpha-1-B glycoprotein",
        "prev_symbol": "",
        "prev_name": "",
        "alias_symbol": "",
        "alias_name": "",
        "agr": "HGNC:5",
        "mane_select": "ENST00000263100.8|NM_130786.4",
    }
    result = extract_lite(test_row)
    assert result == {
        "hgnc_id": "HGNC:5",
        "gene_symbol": "A1BG",
        "gene_name": "alpha-1-B glycoprotein",
        "previous_gene_symbol": [],
        "previous_gene_name": [],
        "alias_symbol": [],
        "alias_name": [],
        "mane_select_transcripts": ["ENST00000263100.8", "NM_130786.4"]
    }


#testing clean()
def test_clean_split():
    result = clean("CCDS7241|CCDS7242|CCDS7243|CCDS73133")
    assert result == ["CCDS7241", "CCDS7242", "CCDS7243", "CCDS73133"]

def test_clean_no_delimiter():
    result = clean("CCDS7241")
    assert result == ["CCDS7241"]

def test_clean_no_value():
    result = clean("")
    assert result == []