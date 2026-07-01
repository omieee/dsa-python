from Problems.valid_palindrome import is_palindrome


def test_if_a_string_is_palindrome() -> None:
    str_to_test = "Was it a car or a cat I saw?"
    assert is_palindrome(str_to_test) is True


def test_valid_palindrome_false_case() -> None:
    assert is_palindrome("race a car") is False


def test_valid_palindrome_only_symbols() -> None:
    assert is_palindrome(".,,") is True


def test_valid_palindrome_mixed_case_digits() -> None:
    assert is_palindrome("0P") is False
