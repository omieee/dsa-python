from Topics_Learning.Stacks.LC_20_Valid_Parenthesis import LC_20_ValidParenthesis


def test_is_valid_parenthesis() -> None:
    lc20vp = LC_20_ValidParenthesis()
    assert lc20vp.isValid("()")
    assert not lc20vp.isValid("({)")
    assert not lc20vp.isValid("([)]")
    assert lc20vp.isValid("([])")
    assert lc20vp.isValid("()[]{}")
