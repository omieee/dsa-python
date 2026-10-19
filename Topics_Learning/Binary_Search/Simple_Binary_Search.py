"""
Question:
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.

APPROACH:

Brute Force: O(n) solution would be loop through the list and check if
target == nums[index] if true
return index else -1

Better Approch:
We will set boundries the first boundry is left index at 0 right is len - 1
and then calculate the mid point which is l + 4 // floor divide by 2
the idea is as we have a sorted list and we know the mid point, so we can ask
where our target is, is it less than the value at mid or greater than value at mid
If it is less then we can shift our right pointer to 1 pos less than mid, If
target is bigger than value at mid, move the left point to 1 pos ahead of mid
That's how we halfed the search area boundry .. this can continue till
left pointer is <= right .. and at that final point target is neither bigger
or smaller.. which means it is equal to target and return the final index
other wise if target is still lower or greater means the while loop will fail in next
run and that target doesnot exist in the list and will return -1

Complexity:
Time: As we are decreasing our length by half we can say complexity is O(logN)
Space: Nothing major extra datastructures gets added hence O(1)


"""


class BinarySearchLinear:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Initial boundry

        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid  # Bingo found the element
        return -1
