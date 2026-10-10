"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
Approach:

Will use stack, and a dictionary to store the matching closed with open
Will run the loop on each characte4r and if the character is not 
in closeToOpen's key that means it's opening and will push directly to stack
once we get a closing.
The reason i will pick the clossing as true is because I want opening should go inside 
stack and our checks are based on clossing ones.
we will see the top of stack is a valid pair of openingBraces of that closing
parenthesis
if true we can discard the top as we found the matrching at correct location
but if it not matches then we will return false as we didn't get the correct opening
braces, at last we can check if there are any opening left in stack that means we are
not having a closing pair left.. we will return False

Complexity
Time: O(n)
SPace: O(n) as we can have n number of openings
"""


class LC_20_ValidParenthesis:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
