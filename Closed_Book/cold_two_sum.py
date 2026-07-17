"""
Given an array of integers nums and an integer target, return the indices
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices
i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input:
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
"""


def cold_two_sum(numbers: list[int], target) -> list[int] | None:
    seen = {}

    for i, v in enumerate(numbers):
        if target - v in seen:
            return [seen[target - v], i]
        else:
            seen[v] = i
    return None


print(cold_two_sum([3, 5, 6, 4], 7))
