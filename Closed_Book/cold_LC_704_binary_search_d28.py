"""
Start: 10:22
Pause: 10:30
Resume: 11:00

Question:
Given an array of integers nums which is sorted in ascending order, and an integer
target, write a function to search target in nums. If target exists, then return its
index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 9

Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input:
nums = [-1, 0, 3, 5, 9, 12]
target = 2

Output: -1
Explanation: 2 does not exist in nums so return -1

Approach:
So we will use binary search because already the list is sorted and we have to find a
thing in that sorted list .. will divide each time the remaing list items to search at
mid and will check if that mid is > target if true that means target is on left will
decree right else will increase left 1 pos to mid

Complexity: O(log n)
"""


class Cold_LC_704_Binary_Search_D_28:
    def search(self, searchList: list[int], target: int) -> int:
        le, ri = 0, len(searchList) - 1

        while le <= ri:
            mid = (le + ri) // 2
            if target > searchList[mid]:
                le = mid + 1
            elif target < searchList[mid]:
                ri = mid - 1
            else:
                return mid
        return -1
