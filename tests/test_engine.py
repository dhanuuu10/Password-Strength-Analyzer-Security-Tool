from analyzer.engine import run_analysis


DATASET_PATH = "data/common_passwords.txt"


def test_complete_password_analysis():

    result = run_analysis(
        "ExampleSecure!789",
        DATASET_PATH
    )

    assert "length" in result
    assert "character_types" in result
    assert "entropy" in result
    assert "score" in result
    assert "classification" in result
    assert "recommendations" in result


def test_common_password_analysis():

    result = run_analysis(
        "password",
        DATASET_PATH
    )

    assert result["is_common_password"] is True
    assert result["score"] < 40


def test_pattern_analysis():

    result = run_analysis(
        "qwerty123",
        DATASET_PATH
    )

    assert result["has_keyboard_pattern"] is True
    assert result["has_sequential_pattern"] is True


def test_analysis_does_not_return_plaintext_password():

    result = run_analysis(
        "Synthetic!Example123",
        DATASET_PATH
    )

    assert "password" not in result