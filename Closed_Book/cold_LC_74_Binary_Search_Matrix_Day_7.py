"""
Start: 10:16
Complete: 10:27

Approach:
So the idea is same like a 1D binary search but this time we will find first
which row could possibly have the target. few things that sugegst why binary search is
good option because the matrix is sorted that means the last index of a row
will always be smaller than 1st element of next row and the Optimum solution
to achieve is O(log(m.n)) that clearly means we need to do two bin search
first to find row and second to find teh actual target in that row


Complexity:
Time O(log(m.n))
Space O(1)

"""


class Cold_LC_74_Bin_Search_Mat_Day_7:
    def clc74bsmd7_search(self, mat: list[list[int]], target: int) -> bool:
        to, bo = 0, len(mat) - 1

        while to <= bo:
            mi = (to + bo) // 2
            if target > mat[mi][-1]:  # last index
                to = mi + 1
            elif target < mat[mi][0]:
                bo = mi - 1
            else:
                break  # found the row
        if to > bo:
            return False
        mi = (to + bo) // 2
        le, ri = 0, len(mat[mi]) - 1

        while le <= ri:
            m = (le + ri) // 2
            if target > mat[mi][m]:
                le = m + 1
            elif target < mat[mi][m]:
                ri = m - 1
            else:
                return True
        return False
