def analyze_length(length):
    """
    Categorize password length.

    This is an educational heuristic, not a guarantee
    of password security.
    """

    if length < 8:
        return {
            "category": "VERY SHORT",
            "message": "Password is shorter than the recommended minimum."
        }

    if length < 12:
        return {
            "category": "SHORT",
            "message": "Consider using a longer password or passphrase."
        }

    if length < 16:
        return {
            "category": "GOOD",
            "message": "Password has a reasonable length."
        }

    return {
        "category": "LONG",
        "message": "Password has strong length characteristics."
    }