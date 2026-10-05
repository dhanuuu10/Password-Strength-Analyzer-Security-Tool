from analyzer.password_analyzer import analyze_password


def test_password_length():
    result = analyze_password("Example123!")

    assert result["length"] == 11


def test_character_types():
    result = analyze_password("Example123!")

    assert result["has_lowercase"] is True
    assert result["has_uppercase"] is True
    assert result["has_digit"] is True
    assert result["has_special"] is True
    assert result["character_types"] == 4


def test_lowercase_only():
    result = analyze_password("password")

    assert result["has_lowercase"] is True
    assert result["has_uppercase"] is False
    assert result["has_digit"] is False
    assert result["has_special"] is False
    assert result["character_types"] == 1


def test_long_password():
    result = analyze_password("ThisIsASyntheticLongPassword")

    assert result["length"] > 20