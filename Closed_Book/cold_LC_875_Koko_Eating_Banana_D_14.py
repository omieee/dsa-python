"""
Start: 12:22 PM
Pause: 2 Min

Problem:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i]
bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some
pile of bananas and eats k bananas from that pile. If the pile has less than k bananas,
 she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the
guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

import math


class Cold_Koko_Eating_Banana_D_14:
    def min_eat_speed(self, piles: list[int], max_hour: int) -> int:
        fastest_speed = max(piles)

        lptr = 1
        rptr = fastest_speed

        while lptr <= rptr:
            m = (lptr + rptr) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= max_hour:
                fastest_speed = min(fastest_speed, m)
                rptr = m - 1
            else:
                lptr = m + 1
        return fastest_speed
