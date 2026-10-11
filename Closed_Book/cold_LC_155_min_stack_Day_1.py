"""
Question: we have to come up with a getMinStack() that gives the minimum values
present at any point in time in a given stack

Approach:
We will use two stack approach, as to give answer in O(1) time
if we loop and find the minimum it will be O(n) approach

So the idea is one stack will hold all the values
where as other stack will store for each i'th the minimum
present at that index. the min stack for each 'i' will be poppulated
at the same time while populating the value stack, but ww will add the minimum of
value and top of minstack.. which ever is lesser will get pushed in to the minstack

while poppoing we wil pop from both index to keep the top of minstack
always valid minimum value present at that point of time and index

getMinFunction will return the top of minstack.

FOllow Up Question: we are wasting space by adding minstack for each

in that case we will add to min stack if the value is <= minstack top value
while popping we wil check if the pooped item is <= minstack top then only we will pop
minstack

Time: O(1) for minStack function
Space: O(n) for value stack and O(n) for minstack

"""


class Cold_LC_155_Sol_Type1_Day1:
    def __init__(self) -> None:
        self.valstack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.valstack.append(val)
        self.minstack.append(min(val, self.minstack[-1] if self.minstack else val))

    def pop(self) -> None:
        self.valstack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.valstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


class Cold_LC_155_Sol_Type2_Day1:
    def __init__(self) -> None:
        self.valstack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.valstack.append(val)
        if self.minstack:
            if val <= self.minstack[-1]:
                self.minstack.append(val)
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        popped = self.valstack.pop()
        if popped <= self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.valstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
