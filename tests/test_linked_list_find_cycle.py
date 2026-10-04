from Topics_Learning.Linked_List import list_node
from Topics_Learning.Linked_List.find_cycle import (
    FindCycleBruteForce,
    FindCycleSlowFastPtr,
)


def test_find_cycle_using_brute_force() -> None:
    fcbr = FindCycleBruteForce()
    assert fcbr.hasCycle(list_node.build_list([3, 2, 0, -4], pos=1))
    assert not fcbr.hasCycle(list_node.build_list([1, 2, 3], pos=-1))
    assert not fcbr.hasCycle(list_node.build_list([], pos=-1))


def test_find_cycle_using_slow_fast_ptr() -> None:
    fcsfp = FindCycleSlowFastPtr()
    assert fcsfp.hasCycle(list_node.build_list([3, 2, 0, -4], pos=1))
    assert not fcsfp.hasCycle(list_node.build_list([1, 2, 3], pos=-1))
    assert not fcsfp.hasCycle(list_node.build_list([], pos=-1))
