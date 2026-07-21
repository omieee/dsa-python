"""
Given prices per day = [10,1,5,6,7,1]
Give the max profit that can be made

max_profit = buy_lowest_on_a_day and sell highest on a latter day

brute force:
max_profit = 0
for loop for buy:
 for loop for sell (starts one day after bought):
  calculate max_profit

better approach:
max_profit = 0
lptr = 0 will act as slow pointer
rptr = 1 will act as fast pointer

while lptr <= len(prices) - 1:
    if prices[lptr] - prices[rptr] > max_proft:
       then max profit is changed
       also rptr moves ahead
    else:
       lptr moves ahead
"""


def best_time_to_buy_and_sell_stock_cold(prices: list[int]) -> int:
    maxprofit = 0
    lptr = 0
    rptr = 1

    while lptr < len(prices) and rptr < len(prices) - 1:
        if prices[rptr] - prices[lptr] > maxprofit:
            maxprofit = prices[rptr] - prices[lptr]
        else:
            lptr += 1
        rptr += 1
    return maxprofit


# print(best_time_to_buy_and_sell_stock_cold([10, 1, 5, 6, 7, 1]))
