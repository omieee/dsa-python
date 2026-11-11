"""
Start: 15:28

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Approach:
Will keep 1 list off all element and another stack that will keep the latest lowest
always on top by inserting the minimum of value and current top at the top and thus
make sure at all index of actuall element the top of min stack will always be the
lowest at that time .. while popping will pop both at the same time just to keep
the lowest always on topand return the top of minStack when asked which is O(1) solution

Complexity:
Space: O(n)
Time: O(1) for all fnction

"""


class Cold_LC_155_Min_Stack_D_28:
    def __init__(self) -> None:
        self.minStk = []
        self.skt = []

    def push(self, val: int) -> None:
        self.skt.append(val)
        self.minStk.append(min(val, self.minStk[-1] if self.minStk else val))

    def pop(self) -> None:
        self.skt.pop()
        self.minStk.pop()

    def top(self) -> int:
        return self.skt[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
