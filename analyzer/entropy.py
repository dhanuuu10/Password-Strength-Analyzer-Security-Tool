import math


def calculate_entropy(password):
    """
    Calculate a theoretical entropy-style estimate.

    This estimate assumes characters were selected randomly
    from the detected character set.

    Human-created passwords may have much lower real-world
    unpredictability than this theoretical estimate suggests.
    """

    if not password:
        return 0.0

    character_set_size = 0

    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    if has_lowercase:
        character_set_size += 26

    if has_uppercase:
        character_set_size += 26

    if has_digit:
        character_set_size += 10

    if has_special:
        character_set_size += 32

    if character_set_size == 0:
        return 0.0

    entropy = len(password) * math.log2(character_set_size)

    return round(entropy, 2)