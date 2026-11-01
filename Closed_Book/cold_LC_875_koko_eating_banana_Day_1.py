import math

"""
Approach. We will run the check from 1 to max possible.
to find what is the lest value of rate
will run a binary search and in that we will chekc how many hours total koko needs to
finish all containers by summing each container's value / rate that is mid 
ex : [30,20,10] let say mid = 10
that means at the rate of 10 he needs three hours to finsish first, 2 hours for second
and 1 hour for the last .. in total it will be 6 hours. if we assume the given hours is
less than 6 which means we can ignore all the right values and try to fid another min on
the left side

TC: O(nlogm)
SC: O(1)

"""


class Cold_LC_875_Koko_Eating_Banana_Day_1:
    def slowestSpeedOfEating(self, containers: list[int], hours: int) -> int:
        slowest, fastest = 1, max(containers)
        kval = fastest
        while slowest <= fastest:
            mid = (slowest + fastest) // 2
            h = 0
            for con in containers:
                h += math.ceil(con / mid)
            if h <= hours:
                kval = min(kval, mid)
                fastest = mid - 1
            else:
                slowest = mid + 1
        return kval
