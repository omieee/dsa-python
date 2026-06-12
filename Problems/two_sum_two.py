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

Solution:

Intuition:

Because the list is sorted we can have two pointers one pointing
left and the other pointing end of list. then we will check if there sum is
greater then or less then the target. If the sum is less then the target
will move right pointer left one position (r -= 1) and then check again.
similarly if target is greater than the sum we will move left pointer right.
(l += 1). Until we find target == sum. If found will return the [l+1,r+1].

Dry Run:

numbers = [1, 2, 3, 4]
target = 3

1.  l = 0, r = len(numbers) - 1
2.  Loop till left is less then right (because adding same number is not the
    solution)
3.  if sum of values at l + r > target means we need to decrease r by 1
4.  if sum of values of l + r < target
5.  if sum of values of l + r == target then return [l+1, r+1]


Big-O Notations:
Time: O(n) we are traversing the list once
Space: O(1) we are just having two extra pointer variables
"""


def two_sum_two(numbers: list[int], target: int) -> list[int] | None:
    le: int = 0
    ri: int = len(numbers) - 1

    while le < ri:
        if numbers[le] + numbers[ri] > target:
            ri -= 1
        elif numbers[le] + numbers[ri] < target:
            le += 1
        else:
            return [le + 1, ri + 1]
