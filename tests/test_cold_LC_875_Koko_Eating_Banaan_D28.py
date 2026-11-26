from Closed_Book.cold_LC_875_Koko_Eating_Banana_D28 import (
    Cold_LC_Koko_Eating_Banana_D28,
)


def test_cold_lc_875_koko_easting_banana_d_1():
    keb = Cold_LC_Koko_Eating_Banana_D28()
    assert 4 == keb.slowestPossibleSpeed([3, 6, 7, 11], 8)
    assert 30 == keb.slowestPossibleSpeed([30, 11, 23, 4, 20], 5)
    assert 23 == keb.slowestPossibleSpeed([30, 11, 23, 4, 20], 6)
    assert 1 == keb.slowestPossibleSpeed([1], 1)
    assert 1 == keb.slowestPossibleSpeed([1, 2], 3)
    assert 1 == keb.slowestPossibleSpeed([4], 4)
