from Closed_Book.cold_LC_875_koko_eating_banana_Day_1 import (
    Cold_LC_875_Koko_Eating_Banana_Day_1,
)


def test_cold_lc_875_koko_easting_banana_d_1():
    keb = Cold_LC_875_Koko_Eating_Banana_Day_1()
    assert 4 == keb.slowestSpeedOfEating([3, 6, 7, 11], hours=8)
    assert 30 == keb.slowestSpeedOfEating([30, 11, 23, 4, 20], hours=5)
    assert 23 == keb.slowestSpeedOfEating([30, 11, 23, 4, 20], hours=6)
    assert 1 == keb.slowestSpeedOfEating([1], hours=1)
    assert 1 == keb.slowestSpeedOfEating([1, 2], 3)
    assert 1 == keb.slowestSpeedOfEating([4], 4)
