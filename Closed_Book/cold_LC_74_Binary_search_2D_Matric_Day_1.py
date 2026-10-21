"""
Approach:
Brute 1: Run a for loop for whole matric O(m.n)
Better 2: Run a for loop for each row and then for that row run the binary search
O(m.logN)
Best 3: Run two binary search one for top to bottom to find which row has the possible
target and only on that row run the second binary search to find the target
O(Log(m.n))

Space on three will be O(1)
"""


class Cold_LC_74_Binary_Search_Matrix_Day_1:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        while t <= b:
            c = (t + b) // 2
            if target > matrix[c][-1]:
                t = c + 1
            elif target < matrix[c][0]:
                b = c - 1
            else:
                break
        if t > b:
            return False
        le, r = 0, len(matrix[c]) - 1
        while le <= r:
            m = (le + r) // 2
            if target > matrix[c][m]:
                le = m + 1
            elif target < matrix[c][m]:
                r = m - 1
            else:
                return True
        return False
