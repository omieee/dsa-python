from Problems.square_of_a_sorted_array import sortedSquares


def test_square_of_sorted_array() -> None:
    assert [0, 1, 9, 16, 100] == sortedSquares(nums=[-4, -1, 0, 3, 10])
    assert [4, 9, 9, 49, 121] == sortedSquares(nums=[-7, -3, 2, 3, 11])
