from Problems.group_anagrams import (
    group_anagrams_brute_force,
    group_anagrams_v2,
)


def test_group_anagrams_brute_force():
    assert group_anagrams_brute_force(["eat", "tea"]) == [["eat", "tea"]]
    assert group_anagrams_brute_force([""]) == [[""]]
    assert group_anagrams_brute_force(["a"]) == [["a"]]


def test_group_anagrams_v2():
    assert group_anagrams_v2(["eat", "tea"]) == [["eat", "tea"]]
    assert group_anagrams_v2([""]) == [[""]]
    assert group_anagrams_v2(["a"]) == [["a"]]


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


def test_group_anagrams_full_case() -> None:
    result = group_anagrams_v2(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]
    assert normalize(result) == normalize(expected)
