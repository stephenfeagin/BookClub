"""
Utility functions
"""
import re

import requests


def strip_isbn(isbn):
    return "".join(re.findall(r"\d", str(isbn)))


def validate_isbn(isbn: str) -> bool:
    bare_isbn = strip_isbn(isbn)

    if len(bare_isbn) == 10:
        digits = list(range(10, 0, -1))
        digit_sum = sum(a*int(b) for a, b in zip(digits, bare_isbn))
        return digit_sum % 11 == 0
    elif len(bare_isbn) == 13:
        digit_sum = 0
        for i in range(len(bare_isbn)):
            if i % 2 == 0:
                digit_sum += int(bare_isbn[i])
            else:
                digit_sum += int(bare_isbn[i])*3
        return digit_sum % 10 == 0
    else:
        return False


def lookup_by_isbn(isbn):
    if not validate_isbn(str(isbn)):
        raise RuntimeError("Invalid ISBN")
    bare_isbn = strip_isbn(isbn)

    url = "https://openlibrary.org/api/books"
    payload = {"bibkeys": f"ISBN:{bare_isbn}", "format": "json", "jscmd": "data"}
    r = requests.get(url, params=payload)

    if r.status_code == 200:
        return r.json()
    else:
        raise RuntimeError(f"No book data found for ISBN {isbn}.")
