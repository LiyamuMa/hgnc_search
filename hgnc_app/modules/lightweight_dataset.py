
import csv
from pathlib import Path

base_directory = Path(__file__).parent.parent
hgnc_complete_set_path = base_directory/"data"/"hgnc_complete_set.txt"

def search(id_or_symbol):
    """
    Reads the hgnc_complete_set.txt file and selects the information needed
    by the hgnc gene information web application. Organises data into Python
    dictionaries that can be used by the application
    """
    with open(hgnc_complete_set_path, newline="", encoding="utf-8") as f:
        hgnc_dict = csv.DictReader(f, delimiter="\t")
        for row in hgnc_dict:
            if id_or_symbol == row["hgnc_id"] or id_or_symbol == row["symbol"]:
                result = extract_lite(row)
                return result


def extract_lite(column):
    """
    Takes a row, keep only columns I want
    """
    return {
        #hgnc_id, gene_symbol, and gene_name are strings
        "hgnc_id": column["hgnc_id"],
        "gene_symbol": column["symbol"],
        "gene_name": column["name"],

        #The rest are lists
        "previous_gene_symbol": clean(column["prev_symbol"]),
        "previous_gene_name": clean(column["prev_name"]),
        "alias_symbol": clean(column["alias_symbol"]),
        "alias_name": clean(column["alias_name"]),
        "mane_select_transcripts": clean(column["mane_select"]),
    }

def clean(cell):
    """
    Takes a cell, split on | if True, return ["N/A"] if False
    """
    if cell:
        return cell.split("|")
    else:
        return []



#handle: did you mean?
