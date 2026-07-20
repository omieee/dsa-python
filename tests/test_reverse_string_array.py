from Problems.reverse_string_array import reverseString


def test_reverse_string_array() -> None:
    assert ["a", "b", "c"] == reverseString("c", "b", "a")
