from ..modules.lightweight_dataset import search, extract_lite, clean

def test_search():
    result = search("A1BG")
    

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