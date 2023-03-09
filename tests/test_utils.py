from libraries.utils import (
    parse_raw_data
)


def test_parse_raw_data():
    """
    Test the example utility function.
    """
    data = "Name: Keke\nAge: 55"
    expected = {
        "Name": "Keke",
        "Age": "55"
    }

    result = parse_raw_data(data)

    assert result == expected
