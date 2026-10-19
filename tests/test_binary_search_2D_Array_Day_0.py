from Topics_Learning.Binary_Search import Matrix_Binary_Search


def test_Binary_Search_2_D_List_Day_0() -> None:
    """
    Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

    Output: true

    Example 2:
    Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

    Output: false
    """
    mbs = Matrix_Binary_Search.BinarySearchMatrix()
    assert mbs.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10)
    assert not mbs.searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15)
