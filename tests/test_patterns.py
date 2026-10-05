from analyzer.pattern_detector import (
    detect_repeated_characters,
    detect_sequential_pattern,
    detect_keyboard_pattern,
)


def test_detect_repeated_characters():
    assert detect_repeated_characters("aaab") is True


def test_detect_repeated_numbers():
    assert detect_repeated_characters("111password") is True


def test_no_excessive_repetition():
    assert detect_repeated_characters("Example123!") is False


def test_short_password():
    assert detect_repeated_characters("aa") is False


def test_detect_ascending_sequence():
    assert detect_sequential_pattern("123456") is True


def test_detect_descending_sequence():
    assert detect_sequential_pattern("987654") is True


def test_detect_letter_sequence():
    assert detect_sequential_pattern("abcdef") is True


def test_no_simple_sequence():
    assert detect_sequential_pattern("Example!9") is False


def test_detect_qwerty_pattern():
    assert detect_keyboard_pattern("qwerty") is True


def test_detect_asdf_pattern():
    assert detect_keyboard_pattern("asdfgh") is True


def test_detect_keyboard_pattern_inside_password():
    assert detect_keyboard_pattern("SecureQwerty123!") is True


def test_no_keyboard_pattern():
    assert detect_keyboard_pattern("Example!9") is False