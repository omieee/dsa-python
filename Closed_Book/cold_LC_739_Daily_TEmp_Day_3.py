"""
Approach is:

We have a given temp list.
We know today and past .. Today decides the past

We will keep a stack and will check the top of stack with today's temp and if we find a
lesser temp anyday in past will pop that and calculate the diffence between days and
store in res for that pooped temperature index

Complexity:
Time: O(n)
Space: O(n)

"""


class Cold_LC_739_Daily_TEmp_Day_3:
    def clLC739D3(self, temp: list) -> list:
        res = [0] * len(temp)
        stk = []  # will store tupple (temp, index)

        for i, t in enumerate(temp):
            while stk and t > stk[-1][0]:
                _, idx = stk.pop()
                res[idx] = i - idx
            stk.append((t, i))
        return res
