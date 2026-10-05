from pathlib import Path


def load_common_passwords(file_path):
    """
    Load common passwords from a local text file.

    Each line represents one password.
    Blank lines and comments are ignored.
    """

    passwords = set()

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Common password file not found: {file_path}"
        )

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            password = line.strip()

            if not password:
                continue

            if password.startswith("#"):
                continue

            passwords.add(password.lower())

    return passwords


def is_common_password(password, common_passwords):
    """
    Check whether a password exists in the common-password dataset.

    Comparison is case-insensitive.
    """

    return password.lower() in common_passwords