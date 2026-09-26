from Closed_Book.cold_ll_cycle import CheckCycle
from Topics_Learning.Linked_List import list_node


def test_find_cycle_using_slow_fast_ptr() -> None:
    cc = CheckCycle()
    assert cc.hasCycle(list_node.build_list([3, 2, 0, -4], pos=1))
    assert not cc.hasCycle(list_node.build_list([1, 2, 3], pos=-1))
    assert not cc.hasCycle(list_node.build_list([], pos=-1))
