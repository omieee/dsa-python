"""
Problem:
Check whether the parenthesis are in correct order of opening and closing
Test Cases / Examples:
s = "((" -> False
s = "()" -> True
s = "(}" -> False
s = "(){}[]" -> True
s = "}" -> False
s = "([)]" -> False
s = "([])" -> True

Approach:

we wil keep a dic of all closing mapped to opening

and then for each character we will check if it is in dict
then we will check the top of stack which will be haing all the openings till that point
of time .. if the top is a valid opening we will pop it out
if not we will return false
at the end if stack is empty we are good all cases are covered
else return false

Ex:
s = "()"
dict = {")": "(", "}": "{", "]": "["}

our loop will run for each character so:
'(' = is not in dict will get pushed to stack
')' = this is in dict. will see if top of stack is matching for it or not in this case
     '('. it matches so we wil pop from stack
at the end the stack is empty will return true

s = "[[]"
our loop will run for each character so:
'[' = is not in dict will get pushed to stack
'[' = is not in dict will get pushed to stack
']' = this is in dict. will see if top of stack is matching for it or not in this case
     '['. it matches so we wil pop from stack
at the end the stack is not empty will return false

Complexity:

time: O(n)
Space: O(n)
"""


class cold_LC_20_Valid_Para_D3:
    def isValid(self, s: str) -> bool:
        stk = []
        clDict = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in clDict:
                if stk:
                    if stk[-1] == clDict[c]:
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            else:
                if c in clDict.values():
                    stk.append(c)
        return True if not stk else False
