from analyzer.password_analyzer import analyze_password
from analyzer.length_analysis import analyze_length
from analyzer.pattern_detector import (
    detect_repeated_characters,
    detect_sequential_pattern,
    detect_keyboard_pattern,
)
from analyzer.common_passwords import (
    load_common_passwords,
    is_common_password,
)
from analyzer.entropy import calculate_entropy
from analyzer.scorer import calculate_score, classify_score
from analyzer.recommendations import generate_recommendations
from analyzer.passphrase import generate_passphrase_guidance


def run_analysis(password, common_password_file):
    """
    Run the complete password analysis pipeline.

    The password is processed only in memory.
    It is not stored, logged, or transmitted.
    """

    # Basic password analysis
    result = analyze_password(password)

    # Length analysis
    result["length_analysis"] = analyze_length(
        result["length"]
    )

    # Pattern detection
    result["has_repeated_characters"] = (
        detect_repeated_characters(password)
    )

    result["has_sequential_pattern"] = (
        detect_sequential_pattern(password)
    )

    result["has_keyboard_pattern"] = (
        detect_keyboard_pattern(password)
    )

    # Common password detection
    common_passwords = load_common_passwords(
        common_password_file
    )

    result["is_common_password"] = (
        is_common_password(
            password,
            common_passwords
        )
    )

    # Entropy-style estimate
    result["entropy"] = calculate_entropy(password)

    # Overall score
    result["score"] = calculate_score(result)

    # Classification
    result["classification"] = classify_score(
        result["score"]
    )

    # Security recommendations
    result["recommendations"] = generate_recommendations(
        result
    )

    # Passphrase guidance
    result["passphrase_guidance"] = (
        generate_passphrase_guidance(password)
    )

    return result