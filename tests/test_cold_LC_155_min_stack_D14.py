from Closed_Book.cold_LC_155_min_stack_D14 import Cold_LC_155_min_stk_d_14


def test_cold_lc_155_min_stack_D14() -> None:
    ms = Cold_LC_155_min_stk_d_14()
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

    ms1 = Cold_LC_155_min_stk_d_14()
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

    ms2 = Cold_LC_155_min_stk_d_14()
    ms2.push(2)
    ms2.push(2)
    min = ms2.getMin()
    ms2.pop()
    top = ms2.top()
    min2 = ms2.getMin()

    assert min == 2
    assert top == 2
    assert min2 == 2

    ms3 = Cold_LC_155_min_stk_d_14()
    ms3.push(5)
    ms3.push(3)
    ms3.push(4)
    ms3.pop()
    top = ms3.top()
    min3 = ms3.getMin()
    assert min3 == 3
