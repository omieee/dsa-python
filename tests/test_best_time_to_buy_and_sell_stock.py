from Problems.best_time_to_buy_and_sell_stock import best_time_to_buy_stock


def test_best_time_to_buy_and_sell_stock() -> None:
    prices = [10, 1, 5, 6, 7, 1]

    assert best_time_to_buy_stock(prices=prices) == 6
