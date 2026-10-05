def generate_passphrase_guidance(password):
    """
    Provide educational guidance about using passphrases.

    This function does not generate or store a password.
    """

    words = password.strip().split()

    if len(words) >= 3:
        return (
            "Passphrase structure detected. Using several "
            "unrelated words can improve memorability and length."
        )

    if len(password) < 12:
        return (
            "Consider using a longer passphrase made from "
            "several unrelated words."
        )

    if len(password) < 16:
        return (
            "A longer passphrase can provide a useful balance "
            "between memorability and length."
        )

    return (
        "A long password or passphrase can provide good "
        "length characteristics."
    )