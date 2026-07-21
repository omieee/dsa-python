"""
Given an array of integers nums and an integer k, return the maximum
average value of a contiguous subarray of size k.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000


Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

Brute Force:
- Iterate through the array and calculate the average of each subarray of size k
- Return the maximum average

Time Complexity: O(n * k)
Space Complexity: O(1)

Sliding Window:
- Initialize a window of size k
- Calculate the average of the window
- Slide the window across the array and calculate the maximum average

Time Complexity: O(n)
Space Complexity: O(1)
"""


def findMaxAverage(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
