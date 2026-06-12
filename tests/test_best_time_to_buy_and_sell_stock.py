from Problems.best_time_to_buy_and_sell_stock import best_time_to_buy_stock


def test_best_time_to_buy_and_sell_stock() -> None:
    prices = [10, 1, 5, 6, 7, 1]

    assert best_time_to_buy_stock(prices=prices) == 6


def test_stock_declining_prices() -> None:
    assert best_time_to_buy_stock([10, 8, 7, 5, 2]) == 0


def test_stock_single_day() -> None:
    assert best_time_to_buy_stock([5]) == 0


def test_stock_common_case() -> None:
    assert best_time_to_buy_stock([7, 1, 5, 3, 6, 4]) == 5
