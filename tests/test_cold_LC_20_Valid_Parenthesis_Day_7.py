from Closed_Book.cold_LC_20_Valid_Parenthesis_Day_7 import LC20_Valid_Parenthesis_D7

"""
Test Cases / Examples:
s = "((" -> False
s = "()" -> True
s = "(}" -> False
s = "(){}[]" -> True
s = "}" -> False
s = "([)]" -> False
s = "([])" -> True
"""


def test_cold_LC20_Day_1() -> None:
    cLC20VPD3 = LC20_Valid_Parenthesis_D7()
    assert not cLC20VPD3.l20vpd7("((")
    assert cLC20VPD3.l20vpd7("()")
    assert cLC20VPD3.l20vpd7("(){}[]")
    assert cLC20VPD3.l20vpd7("([])")
    assert not cLC20VPD3.l20vpd7("(}")
    assert not cLC20VPD3.l20vpd7("}")
    assert not cLC20VPD3.l20vpd7("([)]")
    assert cLC20VPD3.l20vpd7("x{y[z]}")
