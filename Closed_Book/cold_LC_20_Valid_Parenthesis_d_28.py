"""
Approach:
will have  clossing and matching pair dictionary
will also keep all opening parenthesis in a stack
and for each incoming next character if is a key in dict then we chck if tej stack
top is its equal opening

Time: O(n)
Space: O(n)
"""


class cold_LC_20_Valid_Parenthesis_Day_28:
    def clc20vparad28(self, s: str) -> bool:
        op_stk = []
        op_close_pair = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in op_close_pair:
                if op_stk:
                    if op_close_pair[c] == op_stk[-1]:
                        op_stk.pop()
                    else:
                        return False
                else:
                    return False
            else:
                if c in op_close_pair.values():
                    op_stk.append(c)
        return True if not op_stk else False
