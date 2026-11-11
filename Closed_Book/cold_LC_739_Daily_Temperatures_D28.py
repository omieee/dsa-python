"""
Start: 13:25

Question:
Given an array of integers temperatures represents the daily temperatures, return an
array answer such that answer[i] is the number of days you have to wait after the ith
day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.



Example 1:

Input:
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

Output: [1,1,4,2,1,1,0,0]


stk = [(0, 73)]

Complexity: O(n) for both

"""


class Cold_LC_739_Daily_Temp_D28:
    def days_to_wait(self, temp: list[int]) -> list[int]:
        res = [0] * len(temp)  # return list and to start with we can have all 0
        stk = []  # (i, t) will store the day and temp on that day

        for i, t in enumerate(temp):
            # stack should not be empty and top should be < than that days temp
            while stk and stk[-1][1] < t:
                popped = stk.pop()  # if above is true will pop out the lower temp
                # now for that days index will subtrat the current day - that day
                res[popped[0]] = i - popped[0]
            # at last will store current day on stack and this makes stack always
            # hotter to colder
            stk.append((i, t))

        return res
