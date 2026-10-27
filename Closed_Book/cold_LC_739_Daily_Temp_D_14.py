"""
Time: 11:05
Pause:11:16
Resume: 11:20

Approach:
So the idea is to keep all hottest at the start.
First we will create all 0s return list
then will store the index, temp for each index in a stack
for each intery of teamperature we will have an inner loop
that will check if it is greter than the top of stacks's temperature
if that is true we wil calculate the difference in index between current temps index and
the index of temp it is greater than and that difference will be strore for that index
and then we will remove the top of stack

Time: O(n)
Space: O(n)

"""


class Cold_LC_739_Daily_Temp_D_14:
    def clc739dtd14(self, temps: list) -> list:
        res = [0] * len(temps)
        bintemp = []  # (i, t)
        for i, t in enumerate(temps):
            while bintemp and bintemp[-1][1] < t:
                res[bintemp[-1][0]] = i - bintemp[-1][0]
                bintemp.pop()
            bintemp.append((i, t))
        return res
