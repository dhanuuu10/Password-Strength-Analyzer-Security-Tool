def detect_repeated_characters(password):
    """
    Detect excessive repetition of the same character.

    Returns True when the same character appears
    three or more times consecutively.
    """

    if len(password) < 3:
        return False

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False


def detect_sequential_pattern(password):
    """
    Detect simple ascending or descending character sequences.

    Examples detected:
    123
    456
    abc
    xyz
    987
    cba

    This is a basic heuristic and does not identify
    every possible sequential pattern.
    """

    if len(password) < 3:
        return False

    password_lower = password.lower()

    for i in range(len(password_lower) - 2):
        first = ord(password_lower[i])
        second = ord(password_lower[i + 1])
        third = ord(password_lower[i + 2])

        # Ascending sequence
        if second == first + 1 and third == second + 1:
            return True

        # Descending sequence
        if second == first - 1 and third == second - 1:
            return True

    return False
def detect_keyboard_pattern(password):
    """
    Detect common keyboard-row patterns.

    This is a heuristic detector for common keyboard walks.
    It does not attempt to identify every possible keyboard pattern.
    """

    keyboard_patterns = [
        "qwerty",
        "asdfgh",
        "zxcvbn",
        "qwertyui",
        "asdfghjk",
        "zxcvbnm",
        "123456",
        "1234567890",
        "qaz",
        "wsx",
        "edc",
    ]

    password_lower = password.lower()

    for pattern in keyboard_patterns:
        if pattern in password_lower:
            return True

    return False