import math

"""
Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Apprach:
So the idea is to first try to construct the minimum time and maximum time and then find
the best time. minimum time can be 1 and max will be max of pile. Nothing less than 1
is possible atleast koko should eat eat 1 baanan in 1 hour and max pile because that is
for sure he will eat all other bananas pile in less than that.. so now we got a range
to work with. then as usual the binary search would be better solution to minimise the 
number of iterations we will do on this range. Brute force here will be going through
this whole range for each k ata time and find the minimum . and with binary search we
can decrease that iteration. So for binary search we will start with first mid value
say k. andf then calculate if koko would have eater k bananas each hour how manay hours
it would have taken him to finish all .. if he is finish ing early or just in time that
means nothing on right side of k will eaver be able to satisfy our situation but we can
and should still check left to see if any other k can satisfy the minimum number of
bananas each hour and stil finish it. On the othe rhand if number of hours taken is 
more than number of hours given menas koko is eatting slowly and nothing on left will
ever satisfy us and we can discard that and move our search to right

Time complexity: O(nlogm)
Space complexity: O(1)

n is the number of elements in the input (piles)
m is the maximum number of bananas in a pile (max(piles))
"""


class LC_875_Koko_Eating_Banana_Day_0:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        le, r = 1, max(piles)
        res = r  # To start with this will be a deffinit answer

        # will start our binary search
        while le <= r:
            k = (le + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if (
                hours <= h
            ):  # either we have finised eating earlier or just in time, we will see if
                # we can eat any slower and still finish all
                res = min(res, k)  # will save the min of previous slowest and k speed
                r = k - 1  # that means no other possiblity toward sight will be slower
            else:
                # we need to eat faster
                le = k + 1
        return res
