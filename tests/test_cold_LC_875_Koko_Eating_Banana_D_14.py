from Closed_Book.cold_LC_875_Koko_Eating_Banana_D_14 import (
    Cold_Koko_Eating_Banana_D_14,
)


def test_cold_lc_875_koko_easting_banana_d_1():
    keb = Cold_Koko_Eating_Banana_D_14()
    assert 4 == keb.min_eat_speed([3, 6, 7, 11], 8)
    assert 30 == keb.min_eat_speed([30, 11, 23, 4, 20], 5)
    assert 23 == keb.min_eat_speed([30, 11, 23, 4, 20], 6)
    assert 1 == keb.min_eat_speed([1], 1)
    assert 1 == keb.min_eat_speed([1, 2], 3)
    assert 1 == keb.min_eat_speed([4], 4)
