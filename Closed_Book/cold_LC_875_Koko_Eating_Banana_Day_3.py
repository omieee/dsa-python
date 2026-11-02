import math

"""
Approach: written per line
Complexity:
TC: O(nlogm)
SC: O(1)
"""


class Cold_LC_875_Koko_Eating_Banana_Day_3:
    def espeed(self, boxes: list[int], hours: int) -> int:
        # lets find the range
        # slowest will be 1 because eating 0 means not eating at all
        # fastest is the max number in the box
        sl, fa = 1, max(boxes)
        slowest_possible = fa

        # the ideas is now we have a range 1 - max(boxes) so the min can be in between
        while sl <= fa:
            # lets see if at mid quantity wil he be able to finish in given hour
            mi = (sl + fa) // 2
            # lets calculate with given mi how many hours he will take
            h = 0
            for b in boxes:
                h += math.ceil(b / mi)  # koko needs this much time to finish all
            if h <= hours:  # Ohh my god koko can possibly finish faster lets check
                fa = mi - 1
                slowest_possible = min(slowest_possible, mi)
            else:  # Nope mid value is not enoght koko needs to eat little faster
                sl = mi + 1
        return slowest_possible
