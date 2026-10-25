from Topics_Learning.Binary_Search import Simple_Binary_Search


def test_Binary_Search_1_D_List_Day_0() -> None:
    """
    Input: nums = [-1,0,2,4,6,8], target = 4

    Output: 3
    Example 2:

    Input: nums = [-1,0,2,4,6,8], target = 3

    Output: -1
    """
    sbs = Simple_Binary_Search.BinarySearchLinear()
    assert 3 == sbs.search([-1, 0, 2, 4, 6, 8], 4)
    assert -1 == sbs.search([-1, 0, 2, 4, 6, 8], 3)
    assert 5 == sbs.search([-1, 0, 2, 4, 6, 8], 8)
