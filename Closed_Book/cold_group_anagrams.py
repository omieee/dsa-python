"""
Group Anagrams

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""

from collections import defaultdict

seen = defaultdict(list)


def cold_group_anagram(strs: list[str]) -> list[list[str]]:
    if len(strs) < 2:
        return [strs]
    else:
        seen = defaultdict(list)
        for stri in strs:
            sorted_stri = "".join(sorted(stri))
            if sorted_stri in seen.keys():
                seen[sorted_stri].append(stri)
            else:
                seen[sorted_stri].append(stri)
        return list(seen.values())


# print(cold_group_anagram([""]))
# print(cold_group_anagram(["X"]))
# print(cold_group_anagram(["act", "pots", "tops", "cat", "stop", "hat"]))
