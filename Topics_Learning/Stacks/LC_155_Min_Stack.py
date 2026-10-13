"""
Approach:
Initially i thought to use a loop evertime on valstack
to give me the minimum in that stack. That would have made
O(n) time on getMin().

The approach explained by neetcode
is to have two stack and always the smallest will be at top
because before inserting in that stack min stack we will check the top
of min stack with current value

Time: O(1) #for getMin func
Space: O(n) for val and O(n) for min

"""


class MinStack:
    def __init__(self) -> None:
        self.valstack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.valstack.append(val)
        if self.minstack:
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.valstack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.valstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
