"""
Find duplicates there in list or not
Inputs
    nums = [1,2,3,1]
    nums = [1,2,3,4]
    nums = [1,1,1,3,3,4,3,2,4,2]

Outputs
    True
    False
    True


Constraints

1 <= len(nums) <= 10^5
-10^9 <= nums[i] <= 10^9

questions:
1. Can i safelly assume there will never be any alphabets
2.

brute force:
1. I wioll start a loop from 0 to length -1 and then inside i will have 
another loop
 starting again from 0 to length -1 and if the inner index points to the 
 same outer
   index which obviouslly will be the same i will skipo that and if at 
   anyother
     momenbet i see nums[i] == nums[j] where i != j I will return as True 
     else at
       the end will return False

for i in len(nums)-1: #O(n)
  for j in len(nums)-1: # O(n)
    if i != j: #O(1)
      if nums[i] == nums [j]: # O(1)
        return True
return False

Complexity of brute force will be
Time : O(n) + O(n) = O(n2)
Space : Not using anything extra so O(1)

ideal solution:
As i move ahead in loop at the same time i want to check if i have ever 
seen this
 number before or NotSo what we can do is store the number as we go ahead 
 in another
   DS like liust, disct, set and in the next iteration verify whether that 
   exist or not

So what i will choose is list or dict or set etc etc

the problem with liust and set is to check if i have seen or not i have to 
use `in`
 and both list and set will actuallyu iterate over itself to find out .. 
 hence the approch of a hashmap would be more ideal

so here is what i am going to do:

i will start the llop til len -1
will take the index value and check it in our seen deictionary
iof we find it there good else add that value as key and maybe the current 
index where it was as it's value

let try it


# I gave cursor to analyse it and here is the summary:

Summary:
Area: Verdict
Approach: Correct
Logic: Correct
Bug: I → i on line 65
Big O: Correct
Set vs dict reasoning: Set lookup is O(1), not O(n) — worth remembering
Fix the typo, run your three examples, and you should be good.

"""

nums = [1, 1, 1, 2, 2, 3, 4]


def contains_duplicate(nums):
    seen = {}

    for i, v in enumerate(nums):
        if v in seen:
            return True
        else:
            seen[v] = i
    return False
