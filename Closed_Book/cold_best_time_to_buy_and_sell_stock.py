"""
Given prices per day = [10,1,5,6,7,1]
Give the max profit that can be made

max_profit = buy_lowest_on_a_day and sell highest on a latter day

brute force:
max_profit = 0
for loop for buy:
 for loop for sell (starts one day after bought):
  calculate max_profit

"""


def best_time_to_buy_and_sell_stock_cold(prices: list[int]) -> int:
    maxprofit = 0
    min_price = float("inf")

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > maxprofit:
            maxprofit = price - min_price

    return maxprofit


# print(best_time_to_buy_and_sell_stock_cold([10, 1, 5, 6, 7, 1]))
# print(best_time_to_buy_and_sell_stock_cold([7, 1, 5, 3, 6, 4]))
