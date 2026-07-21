from Problems.container_with_most_water import maxArea


def test_max_water() -> None:
    assert 36 == maxArea([1, 7, 2, 5, 4, 7, 3, 6])
    assert 4 == maxArea([2, 2, 2])
