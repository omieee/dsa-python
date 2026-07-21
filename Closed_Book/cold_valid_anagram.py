"""
Valid Anagram
Given two strings s and t, return True if t is an anagram of s, and False
otherwise.

An anagram is a word formed by rearranging the letters of another word,
using all the original letters exactly once.

Example 1

Input:  s = "anagram", t = "nagaram"
Output: True
Example 2

Input:  s = "rat", t = "car"
Output: False
"""

from collections import defaultdict


def cold_valid_anagram(s: str, t: str) -> bool:
    common_place = defaultdict(int)

    for ss in s:
        common_place[ss] += 1
    for tt in t:
        if tt in common_place.keys():
            common_place[tt] -= 1
            if common_place[tt] == 0:
                del common_place[tt]
        else:
            common_place[tt] += 1
    if len(common_place) > 0:
        return False
    else:
        return True


# print(cold_valid_anagram(s="anagram", t="nagaram"))
# print(cold_valid_anagram(s="rat", t="car"))
