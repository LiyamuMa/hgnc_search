
import csv
from pathlib import Path

import logging
logger = logging.getLogger(__name__)
class Error(Exception):
    pass



def search(id_or_symbol):
    
    """
    The function reads the HGNC complete gene set and searches for a
    matching HGNC ID or gene symbol. If a numeric HGNC ID is provided,
    the "HGNC:" prefix is added automatically. The matching row is then
    processed by ``extract_lite()`` and returned as a dictionary.

    Args:
        id_or_symbol: An HGNC ID or gene symbol to search for. A numeric
        HGNC ID can be provided with or without the "HGNC:" prefix.

    Returns:
        A dictionary containing the selected gene information if a match
        is found.

    Raises:
        FileNotFoundError: If the ``hgnc_complete_set.txt`` file cannot
        be found.
    """

    base_directory = Path(__file__).parent.parent
    hgnc_complete_set_path = base_directory/"data"/"hgnc_complete_set.txt"  

    if id_or_symbol.isdigit():
        id_or_symbol = "HGNC:" + id_or_symbol

    try:
        with open(hgnc_complete_set_path, newline="", encoding="utf-8") as f:
            hgnc_dict = csv.DictReader(f, delimiter="\t")
            for row in hgnc_dict:
                if id_or_symbol == row["hgnc_id"] or id_or_symbol == row["symbol"]:
                    result = extract_lite(row)
                    logger.info("Results returned successfully")
                    return result

    except FileNotFoundError as e:
        logger.error("hgnc_complete_set.txt not found")


def extract_lite(column):
  
    """
    Extract the gene information required by the application.

    Args:
        column: A dictionary containing gene information from the HGNC
        complete dataset.

    Returns:
        A dictionary containing the HGNC ID, gene symbol, gene name,
        previous symbols and names, aliases, and MANE Select transcripts.
        String fields are returned as strings, while fields containing
        multiple values are returned as lists.
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
    Split a cell value on "|" if it contains a value.

    Args:
        cell: A cell value to clean.

    Returns:
        A list of values split on "|" if the cell contains a value;
        otherwise, an empty list.
    """

    if cell:
        return cell.split("|")
    else:
        return []

