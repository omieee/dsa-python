from Closed_Book.cold_LC_875_Koko_Eating_Banana_Day_7 import (
    Cold_LC_875_Koko_Eating_Banana_Day_7,
)


def test_cold_lc_875_koko_easting_banana_d_1():
    keb = Cold_LC_875_Koko_Eating_Banana_Day_7()
    assert 4 == keb.slowestgPossible([3, 6, 7, 11], 8)
    assert 30 == keb.slowestgPossible([30, 11, 23, 4, 20], 5)
    assert 23 == keb.slowestgPossible([30, 11, 23, 4, 20], 6)
    assert 1 == keb.slowestgPossible([1], 1)
    assert 1 == keb.slowestgPossible([1, 2], 3)
    assert 1 == keb.slowestgPossible([4], 4)
