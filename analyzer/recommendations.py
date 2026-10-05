def generate_recommendations(analysis):
    """
    Generate security recommendations based on password analysis.

    Recommendations are educational and do not guarantee
    real-world password security.
    """

    recommendations = []

    # Length recommendation
    if analysis["length"] < 8:
        recommendations.append(
            "Use a password that is at least 8 characters long."
        )
    elif analysis["length"] < 12:
        recommendations.append(
            "Consider using a password of 12 or more characters."
        )
    elif analysis["length"] < 16:
        recommendations.append(
            "A longer password or passphrase can provide better protection."
        )

    # Character diversity
    if analysis["character_types"] < 3:
        recommendations.append(
            "Increase character diversity by using different character types."
        )

    # Repeated characters
    if analysis.get("has_repeated_characters", False):
        recommendations.append(
            "Avoid excessive repetition of the same character."
        )

    # Sequential patterns
    if analysis.get("has_sequential_pattern", False):
        recommendations.append(
            "Avoid predictable sequences such as 123 or abc."
        )

    # Keyboard patterns
    if analysis.get("has_keyboard_pattern", False):
        recommendations.append(
            "Avoid common keyboard patterns such as qwerty or asdfgh."
        )

    # Common passwords
    if analysis.get("is_common_password", False):
        recommendations.append(
            "Avoid commonly used passwords because attackers can guess them easily."
        )

    # Strong-password guidance
    if not recommendations:
        recommendations.append(
            "Password shows good characteristics. Continue using unique passwords."
        )

    return recommendations