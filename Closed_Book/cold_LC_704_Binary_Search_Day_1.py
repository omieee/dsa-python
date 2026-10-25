"""
Approach:
Basically we will find whether which side we should look at for the target
we define a search area which starts with full list
and claculate the lower mid (round down) as mid and check if target number is greater
or lesser than nums[mid] if greater we will move left to mid + 1 and if lesser wil move
right to 1 pos less than mid thus decrease the search areay each time by half
when it is neither greater or lesser and le is still less than and equal to right
we can say we found the target and can return mid. else return default -1 as not found

Complexity:
Time: O(logN): as we are decreasing the search area by half each time
Space: O(1)
"""


class Cold_LC_704_Binary_Search_Day_1:
    def search(self, nums: list[int], target: int) -> int:
        # will take left and right boundary
        le, r = 0, len(nums) - 1

        while le <= r:
            mid = (le + r) // 2
            if target > nums[mid]:
                le = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1
