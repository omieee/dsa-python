from Topics_Learning.Linked_List.LC_875_Koko_Eating_Banana import (
    LC_875_Koko_Eating_Banana_Day_0,
)

"""
Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""


def test_koko_eating_banana_day_0() -> None:
    keb = LC_875_Koko_Eating_Banana_Day_0()
    assert 4 == keb.minEatingSpeed([3, 6, 7, 11], h=8)
    assert 30 == keb.minEatingSpeed([30, 11, 23, 4, 20], h=5)
    assert 23 == keb.minEatingSpeed([30, 11, 23, 4, 20], h=6)
    assert 1 == keb.minEatingSpeed([1], h=1)
