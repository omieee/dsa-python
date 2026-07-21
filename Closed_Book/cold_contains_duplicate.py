"""
Given an integer array nums, return true if any value appears more than once in the
array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""

from collections import defaultdict


def find_duplicate(nums: list[int]) -> bool:
    """
    `Brute force:`
    will run a for loop on all nums
    and inside that for loop will run another for loop on nums
    if i == j will skip thee same element
    else if nums[i] == nums[j] means there is a repeat and will return true
    else return false

    `Brute force complexity:
    Space: O(1)
    Time O(n square)`

    ------------------------------------------------------------------------

    Better Approach
    Will have a hashmap where we will add teh elements
    and as soon as we are checking the next element will check it it exist in hash
    if yes its duplicate and return true
    else false

    Complexity:
    Space: O(1)
    Time: O(n) // just one loop and all other lookups are O(1)

    """

    seen = defaultdict(int)

    for i, v in enumerate(nums):
        if v in seen.keys():
            return True
        else:
            seen[v] = i  # If ever you are asked where was the first occurance
    return False


# print(find_duplicate([1, 2, 3, 3]))
# print(find_duplicate([1, 2, 3, 4]))
