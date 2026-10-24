from Closed_Book.cold_LC_74_Binary_search_2D_Matric_Day_1 import (
    Cold_LC_74_Binary_Search_Matrix_Day_1,
)


def test_Binary_Search_2_D_List_Day_0() -> None:
    mbs = Cold_LC_74_Binary_Search_Matrix_Day_1()
    assert mbs.searchMatrix([[5]], 5)
    assert not mbs.searchMatrix([[5]], 2)
    assert not mbs.searchMatrix([[5]], 8)
    assert mbs.searchMatrix([[1, 3, 5, 7]], 7)
    assert not mbs.searchMatrix([[1, 3, 5, 7]], -1)
    assert mbs.searchMatrix([[1], [3], [5], [7]], 3)
    assert not mbs.searchMatrix([[1], [3], [5], [7]], 4)
    assert mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1)
    assert mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60)
    assert mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11)
    assert not mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], -10)
    assert not mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 65)
    assert not mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 8)
    assert not mbs.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 12)
    assert mbs.searchMatrix(
        [[-10000, -5000, -1000], [-500, -100, -50], [-10, 0, 10000]], -10000
    )
    assert mbs.searchMatrix(
        [[-10000, -5000, -1000], [-500, -100, -50], [-10, 0, 10000]], 10000
    )
    assert mbs.searchMatrix(
        [[-10000, -5000, -1000], [-500, -100, -50], [-10, 0, 10000]], -100
    )
    assert not mbs.searchMatrix(
        [[-10000, -5000, -1000], [-500, -100, -50], [-10, 0, 10000]], -200
    )
    assert mbs.searchMatrix([[-10, -5], [-2, 0], [2, 5]], 0)
    assert not mbs.searchMatrix([[-10, -5], [-2, -1], [2, 5]], 0)
