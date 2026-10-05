from analyzer.scorer import calculate_score, classify_score


def test_strong_password_score():
    analysis = {
        "length": 18,
        "character_types": 4,
        "has_repeated_characters": False,
        "has_sequential_pattern": False,
        "has_keyboard_pattern": False,
        "is_common_password": False,
    }

    score = calculate_score(analysis)

    assert score >= 80


def test_common_password_receives_penalty():
    analysis = {
        "length": 12,
        "character_types": 3,
        "has_repeated_characters": False,
        "has_sequential_pattern": False,
        "has_keyboard_pattern": False,
        "is_common_password": True,
    }

    score = calculate_score(analysis)

    assert score < 40


def test_weak_password_score():
    analysis = {
        "length": 6,
        "character_types": 1,
        "has_repeated_characters": True,
        "has_sequential_pattern": True,
        "has_keyboard_pattern": False,
        "is_common_password": False,
    }

    score = calculate_score(analysis)

    assert score < 20


def test_score_stays_between_zero_and_hundred():
    analysis = {
        "length": 50,
        "character_types": 4,
        "has_repeated_characters": False,
        "has_sequential_pattern": False,
        "has_keyboard_pattern": False,
        "is_common_password": False,
    }

    score = calculate_score(analysis)

    assert 0 <= score <= 100


def test_score_classification():
    assert classify_score(10) == "VERY WEAK"
    assert classify_score(30) == "WEAK"
    assert classify_score(50) == "MODERATE"
    assert classify_score(70) == "STRONG"
    assert classify_score(90) == "VERY STRONG"