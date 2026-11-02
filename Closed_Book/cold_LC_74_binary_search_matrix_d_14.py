"""
Approach:
Two phased first time dcoa binary search to find which row can have the solution
to find the row we run through each row and check if target is greater tha last element
a rtow or smaller than first element of each row if greater then wil move top to one
pos next to mid else move bot to one place above mid. once we get the row we will
do another binary search to find the tagete from left to right again via binary search

Complexity
T: O(log(m.n))
S: O(1)
"""


class Cold_LC_74_Binary_Search_Matric_D_14:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Find the row
        to, bo = 0, len(matrix) - 1
        while to <= bo:
            cen = (to + bo) // 2

            if target > matrix[cen][-1]:
                to = cen + 1
            elif target < matrix[cen][0]:
                bo = cen - 1
            else:
                break
        if to > bo:
            return False
        cen = (to + bo) // 2
        le, ri = 0, len(matrix[cen]) - 1

        while le <= ri:
            mi = (le + ri) // 2

            if target > matrix[cen][mi]:
                le = mi + 1
            elif target < matrix[cen][mi]:
                ri = mi - 1
            else:
                return True
        return False
