"""
Problem:

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:
Input: strs = [""]
Output: [[""]]
Example 3:
Input: strs = ["a"]
Output: [["a"]]
=============================================================================


Brute Force Approach:
1. Sort the string
2. Add the sorted string to a dictionary with the original string as the value
3. Return the values of the dictionary

Time Complexity: O(n * m log m)
Space Complexity: O(n * m)

Let's solve one with mental model:
we have a ret of type defaultdict of list (only because we don't want while
insertion
there is a missing index)

Input: strs = ["cat", "tac"]
Will run the for loop for each string in strs
1. Will get first string as `cat` will sort it and it will become `act`
2. then in res {} the key will be `act` and value will append as `cat`
3. loop will pick up next string that is `tac`
4. that will get sorted to `act`
5. then in res {} the value `tac` will be added to the same key `act`

so finally our res {} will look something like this:

res = defaultdict{"act": ["cat", "tac"]}
will return it like res.values() and because we want a list of list we will
return
list(res.values()) which will return [["cat", "tac"]]

Big O Complexity:
Time Complexity: O(n * m log m) - because we are sorting each string and there
are n strings and each string has m characters
Space Complexity: O(n * m) - because we are storing each string in the
dictionary
and there are n strings and each string has m characters

"""

from collections import defaultdict


def group_anagrams_brute_force(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for st in strs:
        res["".join(sorted(st))].append(st)

    return list(res.values())


"""
Now let's solve it with a better Big O complexity

This approach is better than the brute force approach because we are not sorting
each string.
Instead we are using a count array to count the frequency of each character in
the string.

Example:
Input: strs = ["cat", "tac"]

Step 1: We will loop through the `strs`
Step 2: For each string we will create character counter and we know 
        that we can only have 26 englist small character we can create a
        list of 26 zeros
Step 3: Now will loop through each character of the looped `str` from `strs`
Step 4. We need to map the each chartacter in such as way that count[0] 
        actually 
        points to character `a` and count[25] points to character `z`
        So oneapproch to achieve this is we know the unicode runs sequentially
        for `a` to `z`, so we can subtract the unicode of `c` from the string 
        with
        fixed unicode of `a` and then increment that map value by 1
Step 5. So from step 4 for ex for a str = `ace` we will get 
        count = [1,0,1,0,1,....]
Step 6. We Will strore our map in out default dict as 
        res = {(1,0,1,0,1): ["ace"]}
Step 7. Loop will go through other strings and if same key is received it will
        append
Step 8: Now we got all the annagrams pair
Step 9: As problem says give a list of lists we will return 
        list(list(res.values())) 

Dry Run:
Input: strs = ["cat", "tac"]
For first string str = "cat"
    count = [0] * 26
    count[ord("c") - ord("a")] += 1
    count[ord("a") - ord("a")] += 1
    count[ord("t") - ord("a")] += 1
    res = {(1,0,1,0,1,....): ["cat"]}

For second string str = "tac"
    count = [0] * 26
    count[ord("t") - ord("a")] += 1
    count[ord("a") - ord("a")] += 1
    count[ord("c") - ord("a")] += 1
    res = {(1,0,1,0,1,....): ["cat", "tac"]}

return list(res.values()) which will return [["cat", "tac"]]

Big O analysis:
Time Complexity: O(n * m) - because we are looping through each string 
and there are n strings and each string has m characters.

Space Complexity O(n * m) - because we are storing each string in the dictionary
and there are n strings and each string has m characters
"""


def group_anagrams_v2(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return list(res.values())
