from Problems.valid_palindrome import is_palindrome


def test_if_a_string_is_palindrome() -> None:
    str_to_test = "Was it a car or a cat I saw?"
    assert is_palindrome(str_to_test) is True
