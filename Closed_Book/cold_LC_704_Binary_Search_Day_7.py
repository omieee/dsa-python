"""
Start: 10:00 AM
Completed: 10:11

Approach:
So the approach for binary search is two things given in pre-req
1. The list is sorted
2. We are asked to have Time: O(logN) times and this can be achieved
by breaking the list into smaller search area each time the loop is run

So we will define the boundary (left and right) of search and then calculate the mid
If the target is greater than the value at the mid will move the left
pointer to one pos right of mid and search again till left <= right. Similarly
if target is < value at mid will move the right pointer opne pos left of mid
At the end either target will neither be > or < mid means == mid will return mid
else will return -1

Complexity:
Time: O(LogN)
Space: O(1)
"""


class Cold_LC_704_Bin_Search_D_7:
    def cllc704bsd7(self, li: list, ta: int) -> int:
        le, ri = 0, len(li) - 1

        while le <= ri:
            mi = (le + ri) // 2
            if ta > li[mi]:
                le = mi + 1
            elif ta < li[mi]:
                ri = mi - 1
            else:
                return mi
        return -1
