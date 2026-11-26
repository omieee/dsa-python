"""
Approach:
So we have to find what is the slowest possible speed at which koko should eat to finish
all before guard comes

To start we can come up with two clear understanding nothing below 1 is possible and
nothing more than the biggest numberf is piles is required so we got a range 1 to
max(piles) We will calcule the mid speed and see if koko eats at that spped will he be
able to finish the piles and if he is able to finish the pile in less than or equal to
the hours given we can say we found the new slowest at that speed that means nothing
on right of that mid is required and can shrik our right side and if koko takes more
time to finish then noth left of mid will be faster so we can discard the left side

Complexity:
T: O(nlogm)
S: O(1)
"""

import math


class Cold_LC_Koko_Eating_Banana_D28:
    def slowestPossibleSpeed(self, piles: list[int], hour: int) -> int:
        lptr = 1
        rptr = fa = max(piles)

        while lptr <= rptr:
            mi = (lptr + rptr) // 2
            ho = 0
            for p in piles:
                ho += math.ceil(p / mi)
            if ho <= hour:
                fa = min(fa, mi)
                rptr = mi - 1
            else:
                lptr = mi + 1
        return fa
