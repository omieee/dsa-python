from Closed_Book.products_of_array_except_self import (
    productExceptSelfBrute,
    productExceptSelfOptimal,
    productExceptSelfOof1,
)


def test_productExceptSelfBrute():
    assert productExceptSelfBrute([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelfBrute([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_productExceptSelfOptimal():
    assert productExceptSelfOptimal([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelfOptimal([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_productExceptSelfOof1():
    assert productExceptSelfOof1([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelfOof1([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert productExceptSelfOof1([2, 3]) == [3, 2]
