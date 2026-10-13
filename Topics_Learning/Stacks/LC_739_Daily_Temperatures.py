"""
Approach:
So the idea is to keep two stacks
first one being the result stack that has all 0's to satrt with
second stack will kepp a pair of temp and it's index

So we will run the loop for each day's temperature
and inside that loop we will check if temp is greater that top of temperature
if the incomeing temperature is hotter that the top it is popped
and then we calculate how much iterations it took to find a hoter temp than tha
by subtracting i - stack's index

"""


class LC_739_Daily_Temp_Day_0:
    def DailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
