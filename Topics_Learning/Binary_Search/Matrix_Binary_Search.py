"""
Question:
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

Approach:
Brute 1: Go through each and find O(m * n)
Brute 2: We already have single matrix Binary search if we run that inside another for
loop for each row we can achieve O(m * log N)

To achieve O(log(m * n))
We have to achieve log m sam way we did for single list that was left to right this is
top to bottom and find the row that could have the target as the question says each rows
last index will be smaller than next rows starting index.

SO we will calculate top as 0 and bottom as matrix len -1
and we will find miud height and see if the taget is above that height or below that
height .. if below we need to come down so will move top to 1 pos down of mid
else if we need to go up then will move bottom to 1 place above of mid. either we will
find the row or we will loop out wnen top is no more <= bottom in that case the number
will not be in the matrix and can return false other wise we will
run the second binary search on last found row


Complexity:
Time: O(log(m * n))
Space: O(1)
"""


class BinarySearchMatrix:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        TOP, BOT = 0, len(matrix) - 1
        while TOP <= BOT:
            MID = (TOP + BOT) // 2
            if target > matrix[MID][-1]:  # Will check the last index because that tells
                TOP = MID + 1  # WE NEED TO GO DOWN
            elif (
                target < matrix[MID][0]
            ):  # Will check the first index because that tells
                BOT = MID - 1  # WE NEED TO GO UP
            else:
                break  #
        if not TOP <= BOT:
            return False
        MID = (TOP + BOT) // 2
        le, r = 0, len(matrix[MID]) - 1

        while le <= r:
            m = (le + r) // 2
            if target > matrix[MID][m]:
                le = m + 1
            elif target < matrix[MID][m]:
                r = m - 1
            else:
                return True
        return False
