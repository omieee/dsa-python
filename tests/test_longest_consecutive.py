from Problems.longest_consecutive import longest_consecutive


def test_longest_consecutive() -> None:
    assert 4 == longest_consecutive([2, 20, 4, 10, 3, 4, 5])
    assert 7 == longest_consecutive([0, 3, 2, 5, 4, 6, 1, 1])
