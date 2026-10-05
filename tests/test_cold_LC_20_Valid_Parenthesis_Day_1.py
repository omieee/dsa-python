from Closed_Book.cold_LC_20_Valid_Parenthesis_Day_1 import (
    Cold_LC_20_Valid_Parentheses_Day_1,
)

"""
Test Cases / Examples:
s = "()" -> True
s = "(}" -> False
s = "(){}[]" -> True
s = "}" -> False
s = "([)]" -> False
s = "([])" -> True
"""


def test_cold_LC20_Day_1() -> None:
    tcl20d1 = Cold_LC_20_Valid_Parentheses_Day_1()
    assert tcl20d1.isValidD1("()")
    assert tcl20d1.isValidD1("(){}[]")
    assert tcl20d1.isValidD1("([])")
    assert not tcl20d1.isValidD1("(}")
    assert not tcl20d1.isValidD1("}")
    assert not tcl20d1.isValidD1("([)]")
