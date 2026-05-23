'''
Valid Anagram
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

Example 1

Input:  s = "anagram", t = "nagaram"
Output: True
Example 2

Input:  s = "rat", t = "car"
Output: False
Your task

Write a function:

def is_anagram(s, t):
    # your code here
    pass
Constraints

1 <= len(s), len(t) <= 5 * 10^4
s and t consist of lowercase English letters
Bonus questions (same style as your Two Sum notes)

1. What’s the brute-force approach? (sort both strings and compare)
2. Can you avoid sorting? What data structure helps?
3. Time and space complexity for your approach?


Brute Force:

if sorted of s and t is same it's anagram

# s = "anagram"
# t = "nagaram"

s = "car"
t = "cat"

if sorted(s) == sorted(t): # O(n log n)
  print("True")
else:
  print("False)

# Time: O(n log n)
# Space: O(n)

Ideal solution:

if len(s) !- len(t) Return False

run the first loop onb s and store the key value as character : count(occurance)

run a loop on t and for each index value found in seen, decrease the counter for that character until it becomes 1 then
delete the key from hashmap
if at the end all gone means it was an anagram else not an angram

Time Complexity: for two sequential for loops it is O(n) and not O(n2)
Space Complexity: the hashmap will store at most one entry per character so worst case if each character is unique
it will be O(n)

'''



s = "aab"
t = "abb"


def is_anagram(s, t):
    str_counter = {}
    if len(s) != len(t):
        return False
    for v in s: # O(n)
        if v in str_counter: #O(1)
            str_counter[v] += 1 #O(1)
        else:
            str_counter[v] = 1 #O(1)

    for v in t: # O(n)
        if v in str_counter: # O(1)
            if str_counter[v] == 1: #O(1) 
                str_counter.pop(v) #O(1)
            else:
                str_counter[v] -= 1 # O(1)
        else:
            return False
    if(len(str_counter) >= 1): #O(1)
        return False
    return True

print(is_anagram(s, t))


