"""
Approach is in code. Basically the idea is to shrink search boundary
Complexity:
Time = O(logN)
Space = O(1)
"""


class Cold_LC_704_Binary_Search_Day_3:
    def search(self, nums: list[int], target: int) -> int:
        # First will check the boundary
        left, r = 0, len(nums) - 1

        while left <= r:
            m = (left + r) // 2  # get the floor
            if target > nums[m]:  # we will see if that index is lesser than the target
                left = m + 1  # if yes will move left to 1 place ahead of mid
            elif target < nums[m]:  # will see if that index is greater than the target
                r = m - 1  # if yes will move right to 1 please previous of mid
            else:
                return m  # got teh position return
        return -1  # target not found
