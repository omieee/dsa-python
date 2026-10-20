"""
Approach:
will create and all zeros list of same size of temp
then we will keep a stack which will hold
on top always the hotest day, temp (i, t). we will
achieve this by looping through this stack till we find
all coldest and removing them and once we remove we will calculate
tjhe difference of today with that coldest day that is the day
difference

Complexity:
Time: O(n)
Space: O(n)

"""


class Cold_LC_739_Daily_Temp_Day_7:
    def clc739dtd7(self, temp: list) -> list:
        res = [0] * len(temp)
        stk = []  # (i,t)
        for i, t in enumerate(temp):
            while stk and t > stk[-1][1]:
                pi, _ = stk.pop()
                res[pi] = i - pi
            stk.append((i, t))
        return res
