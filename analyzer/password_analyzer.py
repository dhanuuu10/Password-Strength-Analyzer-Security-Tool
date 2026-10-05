import re


def analyze_password(password):
    """
    Perform basic defensive password analysis.

    The password is analyzed only in memory.
    It is not stored, logged, or transmitted.
    """

    length = len(password)

    has_lowercase = bool(re.search(r"[a-z]", password))
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    character_types = sum([
        has_lowercase,
        has_uppercase,
        has_digit,
        has_special
    ])

    result = {
        "length": length,
        "has_lowercase": has_lowercase,
        "has_uppercase": has_uppercase,
        "has_digit": has_digit,
        "has_special": has_special,
        "character_types": character_types,
    }

    return result