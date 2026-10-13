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

    ms1 = MinStack()
    ms1.push(1)
    ms1.push(3)
    ms1.push(5)
    min = ms1.getMin()
    ms1.pop()
    top = ms1.top()
    min2 = ms1.getMin()

    assert min == 1
    assert top == 3
    assert min2 == 1

    ms2 = MinStack()
    ms2.push(2)
    ms2.push(2)
    min = ms2.getMin()
    ms2.pop()
    top = ms2.top()
    min2 = ms2.getMin()

    assert min == 2
    assert top == 2
    assert min2 == 2
