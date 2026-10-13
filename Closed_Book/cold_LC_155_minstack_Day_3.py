"""

Approach: Can be done in 3 ways

Way 1:
we can run the for loop across exiting value stack
every time when ever getMin() is called and find the minimum value
This will give us O(n) Time complexity and O(1) space

Way 2:
We can have two stack and we will push in both stack at same time
But the values we wpush in both is different
valstack will have normal direct push
minstack while pushing we will store the minimum between value and top of min stack
what every minim comes will get pushed for each 'i' inb minstack
This will give us O(1) for getMin() as at any point of time the top of stack will be
the minimum for given 'i' and space will be O(n) .. while poping we have to pop both
stacks to keep minimum true for thye new value top index

Way 3:
This is a case whn the interviewer will say why we are repetatdly wasting memory by
repetedly keeping same element in min stack multiple time .. so in this case
we will push to min stack only when the value <= top of min stack
and pop when popped value == top of min stack. we don't need here <= because that
condition will not come because while inserting only we are making sure by using <=
Here also time is O(n) for a given index
Space O(n) worst case

"""


class Cold_LC_155_Min_STack_Way2_Day3:
    def __init__(self) -> None:
        self.vstack = []
        self.mstack = []

    def push(self, v: int) -> None:
        self.vstack.append(v)
        self.mstack.append(min(v, self.mstack[-1] if self.mstack else v))

    def pop(self) -> None:
        self.vstack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.vstack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]


class Cold_LC_155_Min_STack_Way3_Day3:
    def __init__(self) -> None:
        self.vstack = []
        self.mstack = []

    def push(self, v: int) -> None:
        self.vstack.append(v)
        if self.mstack:
            if v <= self.mstack[-1]:
                self.mstack.append(v)
        else:
            self.mstack.append(v)

    def pop(self) -> None:
        vp = self.vstack.pop()
        if vp == self.mstack[-1]:
            self.mstack.pop()

    def top(self) -> int:
        return self.vstack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]
