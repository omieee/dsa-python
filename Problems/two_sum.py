'''
Two Sum — practice problem

Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.

You may assume:

Each input has exactly one solution
You may not use the same element twice
You can return the answer in any order
Example 1

Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2

Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
Example 3

Input:  nums = [3, 3], target = 6
Output: [0, 1]
Your task

Write a function in two_sum.py:

def two_sum(nums, target):
    # your code here
    pass
Constraints

2 <= len(nums) <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists
Bonus questions to think about (don't answer unless you want feedback):

What is the time complexity of a brute-force approach?
Can you do better than O(n²)? What data structure might help?
What would the space complexity be for your approach?
'''

'''
My Approach

So I have a list and a target . I will iterate through the list and 
will subtract target - cureent index value which will be looked up in a seen 
hashmap .. if it exist we found the item then return the current index and the index of the seen item 
'''

'''
Big O Analysis
Worst Case Scenario:
    If we had followed brute force approach we would have to run nested for loops
    for out loop that would start from n[0] and inner loop would start from n[1] and so on
    for n = 4, we would have to run 4 * 3 = 12 iterations
    Time Complexity: O(n^2)
    Space Complexity: O(1) as we are not using any extra space
    Total Time Complexity: O(n^2) * O(1) = O(n^2)
    Total Space Complexity: O(1)
    This is a worst case scenario as we are not able to find the items in the list in the first iteration itself

Now the following code scenario is better than the brute force approach
Better than O(n^2) because we are able to find the items in the list in the first iteration itself
Time Complexity: O(n)
  - We are iterating through the list once so O(n)
  - We are doing a constant time operation for each iteration so O(1)
  - Total Time Complexity: O(n) * O(1) = O(n)
Space Complexity: O(n)
  - We are using a hashmap to store the seen items so O(n)
  - Total Space Complexity: O(n)
'''



nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
  seen = {} #O(1)
  for i, v in enumerate(nums): #O(n) And as this is the highest time consuming operation so it will be the time complexity
    need_for = target-v #O(1)
    if need_for in seen: #O(1)
      return [seen[need_for], i] #O(1)
    else: #O(1)
      seen[v] = i #O(1)
  return [] #O(1)

