from analyzer.entropy import calculate_entropy


def test_empty_password_entropy():
    assert calculate_entropy("") == 0.0


def test_lowercase_password_entropy():
    result = calculate_entropy("abcdef")

    assert result > 0


def test_mixed_password_entropy():
    result = calculate_entropy("Example123!")

    assert result > 0


def test_longer_password_has_higher_entropy():
    short_password = calculate_entropy("abc123")
    long_password = calculate_entropy("abc123Example456!")

    assert long_password > short_password