"""
Approach
so the approach is to storeall possible closing and opening in dict
and then check if there is match will remove the matching opening from stack
at the ned if the stack is empty we are good
"""


class LC20_Valid_Parenthesis_D7:
    def l20vpd7(self, s: str) -> bool:
        stk = []
        openCloseDict = {"}": "{", "]": "[", ")": "("}

        for c in s:
            if c in openCloseDict:
                if stk:
                    if openCloseDict[c] == stk[-1]:
                        stk.pop()
                    else:
                        return False
                else:
                    return False
            else:
                if c in openCloseDict.values():
                    stk.append(c)
        return True if not stk else False
