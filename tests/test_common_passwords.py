from analyzer.common_passwords import (
    load_common_passwords,
    is_common_password,
)


DATASET_PATH = "data/common_passwords.txt"


def test_common_password_is_detected():
    common_passwords = load_common_passwords(DATASET_PATH)

    assert is_common_password(
        "password",
        common_passwords
    ) is True


def test_common_password_check_is_case_insensitive():
    common_passwords = load_common_passwords(DATASET_PATH)

    assert is_common_password(
        "PASSWORD",
        common_passwords
    ) is True


def test_non_common_password():
    common_passwords = load_common_passwords(DATASET_PATH)

    assert is_common_password(
        "Synthetic!Example9",
        common_passwords
    ) is False