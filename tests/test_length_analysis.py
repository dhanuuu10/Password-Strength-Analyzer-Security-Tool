from analyzer.length_analysis import analyze_length


def test_very_short_password():
    result = analyze_length(6)

    assert result["category"] == "VERY SHORT"


def test_short_password():
    result = analyze_length(10)

    assert result["category"] == "SHORT"


def test_good_length():
    result = analyze_length(14)

    assert result["category"] == "GOOD"


def test_long_password():
    result = analyze_length(20)

    assert result["category"] == "LONG"