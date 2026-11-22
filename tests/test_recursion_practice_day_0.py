from Topics_Learning.Recursion import recursion_practice


def test_check_factorial_5_is_120_day_0() -> None:
    fa = recursion_practice.Recursion_Practice()
    assert 120 == fa.factorial(5)


def test_check_factorial_negative_1_day_0() -> None:
    fa = recursion_practice.Recursion_Practice()
    assert 1 == fa.factorial(-1)


def test_check_factorial_0_day_0() -> None:
    fa = recursion_practice.Recursion_Practice()
    assert 1 == fa.factorial(0)


def test_check_fibbonacci_0_day_0() -> None:
    fib = recursion_practice.Recursion_Practice()
    assert 0 == fib.fibonacci(0)


def test_check_fibbonacci_1_day_0() -> None:
    fib = recursion_practice.Recursion_Practice()
    assert 1 == fib.fibonacci(1)


def test_check_fibbonacci_2_day_0() -> None:
    fib = recursion_practice.Recursion_Practice()
    assert 1 == fib.fibonacci(2)
