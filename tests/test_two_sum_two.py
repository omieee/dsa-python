from Problems.two_sum_two import two_sum_two


def test_get_position_of_two_sum() -> None:
    numbers = [1, 2, 3, 4]
    target = 3
    assert two_sum_two(numbers=numbers, target=target) == [1, 2]
