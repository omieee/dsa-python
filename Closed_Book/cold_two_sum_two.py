"""
Problem Statement:

Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such that they
add up to a given target number target and index1 < index2. Note that index1 and
index2 cannot be equal, therefore you may not use the same element twice.

Ex:
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]

Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, index1 = 1,
index2 = 2. We return [1, 2].

Constraints:
    2 <= numbers.length <= 1000
    -1000 <= numbers[i] <= 1000
    -1000 <= target <= 1000
"""


def two_sum_two(nums: list[int], target: int) -> list[int]:
    lptr = 0
    rptr = len(nums) - 1

    while rptr > lptr:
        if nums[lptr] + nums[rptr] == target:
            return [lptr + 1, rptr + 1]
        elif nums[lptr] + nums[rptr] > target:
            rptr -= 1
        else:
            lptr += 1


# print(two_sum_two([2, 7, 11, 15], 9))
# print(two_sum_two([2, 3, 4], 6))
print(two_sum_two([1, 2, 4], 4))
