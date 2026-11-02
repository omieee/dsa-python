"""
Approach:
We will run a loop through the range from starting to the end of given list
we will see if the center of current evaluting range is greater or lesser then target
If target is greater than mid than it means the result will no chance be on the left
of mid so we can remove the search area of left and move left to 1 pos mid and if lesser
then move the right to 1 pos left of mid .. if neigher is correct then we mid have found
the target and return it

Complexity:
T = O(logN)
S = O(1)
"""


class Cold_LC_704_Binary_Search_D_14:
    def search(self, nums: list[int], target: int) -> int:
        le, ri = 0, len(nums) - 1

        while le <= ri:
            mi = (le + ri) // 2
            if target > nums[mi]:
                le = mi + 1
            elif target < nums[mi]:
                ri = mi - 1
            else:
                return mi
        return -1
