from Problems.group_anagrams import groupAnagramsBruteForce, groupAnagramsV2

def test_group_anagrams_brute_force():
    assert groupAnagramsBruteForce(["eat","tea"]) == [["eat","tea"]]
    assert groupAnagramsBruteForce([""]) == [[""]]
    assert groupAnagramsBruteForce(["a"]) == [["a"]]

def test_group_anagrams_v2():
    assert groupAnagramsV2(["eat","tea"]) == [["eat","tea"]]
    assert groupAnagramsV2([""]) == [[""]]
    assert groupAnagramsV2(["a"]) == [["a"]]