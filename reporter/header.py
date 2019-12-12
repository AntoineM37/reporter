
import datetime
import warnings
import json


def _validate(author):
    #if {"first", "last"}.issubset(author):
    #    return True
    #else:
    
    missing = {"first", "last"}.difference(author)
    if not missing:
        return True
    for miss in missing:
        warnings.warn(f"Key {miss} is missing")
    return False

def create_header(authors, city="Paris"):
    """Returns the header string
    
    This function creates a header string with today's date
    and the names of the authors.
    
    Parameters
    ----------
    authors : list of dictionnaries
        Each dict should have at least the keys 
        'first' and 'last'
    city : str, optional, default 'Paris'
        The city from which the report is emitted
        
    Returns
    -------
    header_string : str
        the header string ...
        
    Example
    -------
    >>> authors = [{}, {}]
    >>> res = cre...
    
    """
    
    today = datetime.date.today().strftime('%d/%m/%Y')
    lines = [f"{city}, le {today}", "\n", "### Authors:"]
    for author in authors:
        _validate(author)
        first = author.get("first", "XX")
        last = author.get("last", "XX")
        lines.append(f"- {first} {last}")
    return "\n".join(lines)