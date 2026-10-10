from Topics_Learning.Stacks.LC_155_Min_Stack import MinStack


def test_lc_155_min_stack() -> None:
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    min = ms.getMin()
    ms.pop()
    top = ms.top()
    min2 = ms.getMin()

    assert min == -3
    assert top == 0
    assert min2 == -2
