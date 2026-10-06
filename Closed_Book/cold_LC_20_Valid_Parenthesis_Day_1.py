"""
Problem:
Check whether the parenthesis are in correct order of opening and closibg
Test Cases / Examples:
s = "()" -> True
s = "(}" -> False
s = "(){}[]" -> True
s = "}" -> False
s = "([)]" -> False
s = "([])" -> True

Procedure:
We will use stack to keep all opening braces and as soon as we see a closing one.
We will also keep a dictionaly that maps closing with it's opening
we will check if the top of stack is equal opening of that closing braces.
If yes we will pop that opening from top
If no will return False
At last we will check if the stack is empty. means no opening is left in stack
If empty return True else return false

Complexity:
Time: O(n): we are traversing all the character of string
Space: O(n): In worst case we might need to store all opening braces in stack
"""


class Cold_LC_20_Valid_Parentheses_Day_1:
    def isValidD1(self, s: str) -> bool:
        openingStack = []
        closeOpenMappingDict = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if c in closeOpenMappingDict:
                if openingStack and openingStack[-1] == closeOpenMappingDict[c]:
                    openingStack.pop()
                else:
                    return False
            else:
                if c in closeOpenMappingDict.values():
                    openingStack.append(c)
        return True if not openingStack else False
