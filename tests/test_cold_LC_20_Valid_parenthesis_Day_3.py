from Closed_Book.cold_LC_20_Valid_Parenthesis_Day_3 import cold_LC_20_Valid_Para_D3

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
    cLC20VPD3 = cold_LC_20_Valid_Para_D3()
    assert not cLC20VPD3.isValid("((")
    assert cLC20VPD3.isValid("()")
    assert cLC20VPD3.isValid("(){}[]")
    assert cLC20VPD3.isValid("([])")
    assert not cLC20VPD3.isValid("(}")
    assert not cLC20VPD3.isValid("}")
    assert not cLC20VPD3.isValid("([)]")
    assert cLC20VPD3.isValid("x{y[z]}")
