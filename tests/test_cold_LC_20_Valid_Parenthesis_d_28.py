from Closed_Book.cold_LC_20_Valid_Parenthesis_d_28 import (
    cold_LC_20_Valid_Parenthesis_Day_28,
)


def test_cold_LC_20_V_P_D_28():
    cLC20VPD28 = cold_LC_20_Valid_Parenthesis_Day_28()
    assert not cLC20VPD28.clc20vparad28("((")
    assert cLC20VPD28.clc20vparad28("()")
    assert cLC20VPD28.clc20vparad28("(){}[]")
    assert cLC20VPD28.clc20vparad28("([])")
    assert not cLC20VPD28.clc20vparad28("(}")
    assert not cLC20VPD28.clc20vparad28("}")
    assert not cLC20VPD28.clc20vparad28("([)]")
    assert cLC20VPD28.clc20vparad28("x{y[z]}")
    assert not cLC20VPD28.clc20vparad28("(])")
