"""
Start: 11:07 AM
Approach:

We wil have a stack where we will push all the opening brackets by filturing out the
closing one as explained below and also will filter outr any other character that is
not a opening bracket

Now we will have aclosising braket keyed dict whoese keys are closing bracket and value
is the correct opening bracket. Then we will loop characcter by character and wil check
if the character is present in the dict key, if yes then we will check if there are any
thing existing in stack or not. we can't reverse this check because if the first char
is a closing bracket  we have to return false .. else we will check if the top of stack
is same as value of that 'c' dict key.. if that matches we have found a valid closing
opening pair at correct location and can pop off else we can return False.
at the end of loop we can see if anything is pending in stack and return True if empty
else False

Complexity:
Time: O(n)
Space: O(n)

"""


class cold_LC_20_Valid_Parenthesis_Day_14:
    def clc20vpd14(self, s: str) -> bool:
        close_open_rule = {"]": "[", "}": "{", ")": "("}
        all_open_stack = []

        for c in s:
            if c in close_open_rule:
                if all_open_stack:
                    if all_open_stack[-1] == close_open_rule[c]:
                        all_open_stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                if c in close_open_rule.values():
                    all_open_stack.append(c)
        return True if not all_open_stack else False
