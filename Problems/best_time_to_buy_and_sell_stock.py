"""
Problem:

You are given an integer array prices where prices[i] is the price of SomeCoin
on the ith day.

You may choose a single day to buy one SomeCoin and choose a different day in
the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any
transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100

Solution:

Intuition:
Stock prices move by day so buying today and selling yesterday is not possible
explicitly.
So what we can check is let say i buy today(left) and sell tomorrow (right)
and record the max profit. If today is greater than tomorrow means we can
move today and tomorrow by one place.
Now let say we move max profit of 10 Rs with us.
We will move the right pointer one place at a time and recalculate max profit.
if the current profit is not more than max profit we will continue moving to
right.

Dry Run:
prices = [10,1,5,6,7,1]
Output = 6

1.  l = 0, r = len(prices) - 1
2.  run a for loop from start of prices to the end
3.  if prices[l] > prices[r], means we are not buying at best price
    we will move l and r by 1 place
4.  if profit < prices[r] - prices[l]
    profit = prices[r] - prices[l]
5.  we keep on moving r till the end


Big-O Notations:
Time: O(n) we are traversing the list once
Space: O(1) we are just having two extra pointer variables and one profit
"""


def best_time_to_buy_stock(prices: list[int]) -> int:
    le = 0
    ri = 1
    p = 0
    for _ in range(0, len(prices) - 1):
        if prices[ri] < prices[le]:
            le = ri
            ri += 1
        else:
            if prices[ri] - prices[le] > p:
                p = prices[ri] - prices[le]
            ri += 1

    return p
