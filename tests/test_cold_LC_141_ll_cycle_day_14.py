from Closed_Book.cold_LC_141_ll_cycle_day_14 import ColdLLCycleD14
from Topics_Learning.Linked_List import list_node


def test_cold_find_cycle_fast_slow_ptr() -> None:
    clld14 = ColdLLCycleD14()
    assert clld14.hasCycle(list_node.build_list([3, 2, 0, -4], pos=1))
    assert not clld14.hasCycle(list_node.build_list([1, 2, 3], pos=-1))
    assert not clld14.hasCycle(list_node.build_list([], pos=0))
    assert clld14.hasCycle(list_node.build_list([3], pos=0))
