"""
Time Docs:
Start: 10:39 AM
Pause: 10:45 - 10:59 Had to go to make my son sleep
Resule: 11:00 AM


Approach:
Brute: find the min from traversing the given list O(n2) times that will give O(n2)
Time complexity, and O(1) space.. We can optimise for O(1) time and space
O(n) or even O(<n)

Optimal Solution:
have a parallel stack in Type one push the minimum of top and val into mstack and pop
both this keeps the top of mstack always the minimum, because we do min while pushing
In the second way we try to save space by only inserting when the value is less then
or equal to top of m stack and pop mstack only when popped is equal to top of mstack

Complexity:
Time: O(1) in both Optimum solution
Space O(n) exactly as we store the second stack exact n times and for space saver we
have O(<=n)


"""


class Cold_LC_155_Min_Stack_Day_7_Type_1:
    def __init__(self) -> None:
        self.vstack = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.vstack.append(val)
        self.mstk.append(min(val, self.mstk[-1] if self.mstk else val))

    def pop(self) -> None:
        self.vstack.pop()
        self.mstk.pop()

    def top(self) -> int:
        return self.vstack[-1]

    def getMin(self) -> int:
        return self.mstk[-1]


class Cold_LC_155_Min_Stack_Day_7_Type_2:
    def __init__(self) -> None:
        self.vstack = []
        self.mstk = []

    def push(self, val: int) -> None:
        self.vstack.append(val)
        if self.mstk:
            if val <= self.mstk[-1]:
                self.mstk.append(val)
        else:
            self.mstk.append(val)

    def pop(self) -> None:
        p = self.vstack.pop()
        if p == self.mstk[-1]:
            self.mstk.pop()

    def top(self) -> int:
        return self.vstack[-1]

    def getMin(self) -> int:
        return self.mstk[-1]
