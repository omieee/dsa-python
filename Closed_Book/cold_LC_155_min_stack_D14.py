"""
Time: 11:07
Break Start: 11:09
Resume: 11:18

Approach:
Last time it took 34 min because i gave 2 solution one for exact O(n) space one for
upto O(n) space by not inserting every other repeted element in binstack

So now while pushing we are pushing in both stacks at the same time and in binstk
we are taking a minimum of val and top of bin stack and pushing and similarly while
popping will pop from both

Complexity:
For getMin Time is O(1)
Space: O(n)

"""


class Cold_LC_155_min_stk_d_14:
    def __init__(self) -> None:
        self.vstk = []
        self.binstk = []

    def push(self, val: int) -> None:
        self.binstk.append(min(val, self.binstk[-1] if self.binstk else val))
        self.vstk.append(val)

    def pop(self) -> None:
        self.vstk.pop()
        self.binstk.pop()

    def top(self) -> int:
        return self.vstk[-1]

    def getMin(self) -> int:
        return self.binstk[-1]
