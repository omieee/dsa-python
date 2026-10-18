from Closed_Book.cold_LC_20_Valid_Parenthesis_Day_14 import (
    cold_LC_20_Valid_Parenthesis_Day_14,
)

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
    cLC20VPD14 = cold_LC_20_Valid_Parenthesis_Day_14()
    assert not cLC20VPD14.clc20vpd14("((")
    assert cLC20VPD14.clc20vpd14("()")
    assert cLC20VPD14.clc20vpd14("(){}[]")
    assert cLC20VPD14.clc20vpd14("([])")
    assert not cLC20VPD14.clc20vpd14("(}")
    assert not cLC20VPD14.clc20vpd14("}")
    assert not cLC20VPD14.clc20vpd14("([)]")
    assert cLC20VPD14.clc20vpd14("x{y[z]}")
