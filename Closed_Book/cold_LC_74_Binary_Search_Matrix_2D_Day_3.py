"""
Approach:
will run two binary search
1. to find which row can have the value
2. does that row have the value

complexity:
Time: o(Log(m.n))
Space: O(1)
"""


class Cold_LC_74_Bin_Search_Mat_2d_Day_3:
    def clc74bsm2dd3_search(self, mat: list[list[int]], target: int) -> bool:
        to, bo = 0, len(mat) - 1
        m = 0
        while to <= bo:
            m = (to + bo) // 2
            if target > mat[m][-1]:
                to = m + 1
            elif target < mat[m][0]:
                bo = m - 1
            else:
                break
        if to > bo:
            return False
        le, r = 0, len(mat[m]) - 1
        while le <= r:
            mi = (le + r) // 2
            if target > mat[m][mi]:
                le = mi + 1
            elif target < mat[m][mi]:
                r = mi - 1
            else:
                return True
        return False
