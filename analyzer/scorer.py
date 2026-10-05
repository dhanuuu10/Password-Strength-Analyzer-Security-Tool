def calculate_score(analysis):
    """
    Calculate an overall password-strength score.

    The score is an educational heuristic based on:
    - password length
    - character diversity
    - repeated characters
    - sequential patterns
    - keyboard patterns
    - common-password detection

    The score is not a guarantee of real-world security.
    """

    score = 0

    # Length
    length = analysis["length"]

    if length >= 16:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        score += 5

    # Character diversity
    character_types = analysis["character_types"]

    if character_types == 4:
        score += 30
    elif character_types == 3:
        score += 22
    elif character_types == 2:
        score += 12
    else:
        score += 5

    # Pattern penalties
    if analysis.get("has_repeated_characters", False):
        score -= 10

    if analysis.get("has_sequential_pattern", False):
        score -= 10

    if analysis.get("has_keyboard_pattern", False):
        score -= 10

    # Common-password penalty
    if analysis.get("is_common_password", False):
        score -= 30

    # Bonus for having no detected weaknesses
    if (
        not analysis.get("has_repeated_characters", False)
        and not analysis.get("has_sequential_pattern", False)
        and not analysis.get("has_keyboard_pattern", False)
        and not analysis.get("is_common_password", False)
    ):
        score += 10

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    return score


def classify_score(score):
    """
    Convert a numerical score into a strength category.
    """

    if score < 20:
        return "VERY WEAK"

    if score < 40:
        return "WEAK"

    if score < 60:
        return "MODERATE"

    if score < 80:
        return "STRONG"

    return "VERY STRONG"