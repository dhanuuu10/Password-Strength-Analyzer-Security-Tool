from analyzer.passphrase import generate_passphrase_guidance


def test_short_password_gets_passphrase_guidance():
    result = generate_passphrase_guidance("abc123")

    assert "longer passphrase" in result


def test_medium_password_gets_guidance():
    result = generate_passphrase_guidance("Example123!")

    assert "passphrase" in result


def test_long_password_gets_length_guidance():
    result = generate_passphrase_guidance(
        "ExampleSecurePassword123!"
    )

    assert "length" in result


def test_multiple_words_detected():
    result = generate_passphrase_guidance(
        "river cloud forest lantern"
    )

    assert "Passphrase structure detected" in result