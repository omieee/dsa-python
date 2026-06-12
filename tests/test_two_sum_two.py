from Problems.two_sum_two import two_sum_two


def test_two_sum_two_pair_at_edges() -> None:
    assert two_sum_two([2, 7, 11, 15], 9) == [1, 2]


def test_two_sum_two_with_negatives() -> None:
    assert two_sum_two([-4, -1, 0, 3, 10], 2) == [2, 4]


def test_two_sum_two_duplicate_values() -> None:
    assert two_sum_two([1, 1, 3, 4], 2) == [1, 2]
