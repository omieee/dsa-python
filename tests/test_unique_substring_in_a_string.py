from Problems.unique_substring_in_a_string import lengthOfLongestSubstring

def test_unique_substring_in_a_string() -> None:
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring("au") == 2
    assert lengthOfLongestSubstring("dvdf") == 3
    assert lengthOfLongestSubstring("aab") == 2
    assert lengthOfLongestSubstring("abba") == 2
    assert lengthOfLongestSubstring("abcabcbb") == 3