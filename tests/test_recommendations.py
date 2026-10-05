from analyzer.recommendations import generate_recommendations


def test_short_password_recommendation():
    analysis = {
        "length": 6,
        "character_types": 1,
        "has_repeated_characters": False,
        "has_sequential_pattern": False,
        "has_keyboard_pattern": False,
        "is_common_password": False,
    }

    recommendations = generate_recommendations(analysis)

    assert len(recommendations) > 0
    assert any("8 characters" in item for item in recommendations)


def test_common_password_recommendation():
    analysis = {
        "length": 12,
        "character_types": 3,
        "has_repeated_characters": False,
        "has_sequential_pattern": False,
        "has_keyboard_pattern": False,
        "is_common_password": True,
    }

    recommendations = generate_recommendations(analysis)

    assert any("commonly used" in item for item in recommendations)


def test_pattern_recommendation():
    analysis = {
        "length": 12,
        "character_types": 4,
        "has_repeated_characters": True,
        "has_sequential_pattern": True,
        "has_keyboard_pattern": False,
        "is_common_password": False,
    }

    recommendations = generate_recommendations(analysis)

    assert any("repetition" in item for item in recommendations)
    assert any("sequences" in item for item in recommendations)


def test_strong_password_recommendation():
    analysis = {
        "length": 18,
        "character_types": 4,
        "has_repeated_characters": False,
        "has_sequential_pattern": False,
        "has_keyboard_pattern": False,
        "is_common_password": False,
    }

    recommendations = generate_recommendations(analysis)

    assert len(recommendations) == 1
    assert "good characteristics" in recommendations[0]