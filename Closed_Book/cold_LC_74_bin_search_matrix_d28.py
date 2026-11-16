"""
Start: 11:05
Question:

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input:
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

Output: true

Approach:
Binary search first top down as the whole matrix is sorted then left right on possible
row

Complexity:
Time: O(log(m.n))
Space: O(1)
"""


class Cold_LC_74_bin_mat_search_d_28:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        to, bo = 0, len(matrix) - 1

        while to <= bo:
            mi = (to + bo) // 2
            if target < matrix[mi][0]:
                bo = mi - 1
            elif target > matrix[mi][-1]:
                to = mi + 1
            else:
                break  # This is the possible row

        if to > bo:
            return False
        mi = (to + bo) // 2
        le, ri = 0, len(matrix[mi]) - 1

        while le <= ri:
            mid = (le + ri) // 2
            if target > matrix[mi][mid]:
                le = mid + 1
            elif target < matrix[mi][mid]:
                ri = mid - 1
            else:
                return True
        return False
