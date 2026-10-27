from Closed_Book.cold_LC_704_Binary_Search_Day_7 import (
    Cold_LC_704_Bin_Search_D_7,
)


def test_Binary_cllc704bsd7_1_D_List_Day_0() -> None:
    sbs = Cold_LC_704_Bin_Search_D_7()
    assert 3 == sbs.cllc704bsd7([-1, 0, 2, 4, 6, 8], 4)
    assert -1 == sbs.cllc704bsd7([-1, 0, 2, 4, 6, 8], 3)
    assert 5 == sbs.cllc704bsd7([-1, 0, 2, 4, 6, 8], 8)
    assert 0 == sbs.cllc704bsd7([5], 5)
    assert -1 == sbs.cllc704bsd7([5], -10)
    assert 0 == sbs.cllc704bsd7([-2, 2], -2)
    assert 1 == sbs.cllc704bsd7([-2, 2], 2)
    assert -1 == sbs.cllc704bsd7([-5, 0, 3, 9], -10)
    assert -1 == sbs.cllc704bsd7([-5, 0, 3, 9], 15)
    assert -1 == sbs.cllc704bsd7([-10, -5, 2, 8, 15], 0)
    assert 3 == sbs.cllc704bsd7([-9999, -500, -20, -5], -5)
    assert 1 == sbs.cllc704bsd7([1, 100, 9999], 100)
    assert 1 == sbs.cllc704bsd7([-100, 0, 100], 0)
    assert 2 == sbs.cllc704bsd7([10, 20, 30, 40, 50, 60], 30)
    assert 3 == sbs.cllc704bsd7([10, 20, 30, 40, 50, 60], 40)
    assert 0 == sbs.cllc704bsd7([-9999, 0, 9999], -9999)
    assert 2 == sbs.cllc704bsd7([-9999, 0, 9999], 9999)
    assert 2 == sbs.cllc704bsd7([-10, -5, 0, 5, 10], 0)
    assert 9999 == sbs.cllc704bsd7(list(range(-5000, 5000)), 4999)
    assert -1 == sbs.cllc704bsd7(list(range(-5000, 5000)), 5000)
