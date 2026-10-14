"""
Approach:

First we will have a res stack of all zeros
and then we will have anoth bin stack that will store
a list of tupples in format temp, index

we will loop through the temperature list.
if bin stack is empty will just push the the latest temp in bin stack as (temp, index)

else we will see if the top of bin stack temp is lower than todays temp
if yes then we will claulate how many days it took to find the hotest
by subrtacting when was that top bin stack temp recorded by it's index and and subtract
it from today's index

ex: let say sunday os 0 and saturday is 7
if tuesday[2] was 38 and thursday[4] was 39
so res is 4-2 = 2 it took two days from tues to find a new hottest

and then we pop of that entry from bin stack and return our result

Complexity:
O(n): we are looping the outer loop only once and the inner while loop is poping once
and never re visting that index

For space also O(n)

"""


class Cold_LC_739_Daily_Temp_Day_1:
    def cl79dtd1(self, temp: list[int]) -> list[int]:
        res = [0] * len(temp)
        binstk = []  # We will store tupple(temp, index)

        for i, t in enumerate(temp):
            while binstk and binstk[-1][0] < t:
                # we could use pop as neetcode does, but this is me
                res[binstk[-1][1]] = i - binstk[-1][1]
                binstk.pop()
            binstk.append((t, i))
        return res
