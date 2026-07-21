"""
Problem
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division
operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Brute Force Solution:
- Time Complexity: O(n^2)
- Space Complexity: O(n)

Optimal Solution:
- Time Complexity: O(n)
- Space Complexity: O(n)

Brute Force Approach:
We can use two nested loops to calculate the product of all the elements except the
current element.
for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            product *= nums[j]
    result.append(product)

return result

Optimal Approach:
For O(n) time complexity and O(n) space complexity, we can use two arrays to store the
product of the elements before and after the current element.
left_product = [1] * len(nums) # Initialize the left product array with 1
right_product = [1] * len(nums) # Initialize the right product array with 1
# Explain in detail what is happening from here in each line in depth comments
for i in range(1, len(nums)):
    left_product[i] = left_product[i-1] * nums[i-1]
for i in range(len(nums)-2, -1, -1):
    right_product[i] = right_product[i+1] * nums[i+1]
return [left_product[i] * right_product[i] for i in range(len(nums))]
return result
"""


def productExceptSelfBrute(nums: list[int]) -> list[int]:
    retlist = []
    for i, _ in enumerate(nums):
        calculation = 1
        for j, val2 in enumerate(nums):
            if i != j:
                calculation *= val2
        retlist.append(calculation)
    return retlist


def productExceptSelfOptimal(nums: list[int]) -> list[int]:
    left_products = [1] * len(nums)
    right_products = [1] * len(nums)

    for i in range(1, len(nums)):
        # The left product of the current element is the product of the previous element
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        # The right product of the current element is the product of the next element
        right_products[i] = right_products[i + 1] * nums[i + 1]
    # The result is the product of the left and right products
    return [left_products[i] * right_products[i] for i in range(len(nums))]


def productExceptSelfOof1(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    for i in range(1, len(nums)):
        result[i] = result[i - 1] * nums[i - 1]
    suffix_product = 1
    for i in range(len(nums) - 2, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]
    return result
