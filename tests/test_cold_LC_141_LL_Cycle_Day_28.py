from Closed_Book.cold_LC_141_LL_Cycle_Day_28 import ColdLC141LLCycleDay28
from Topics_Learning.Linked_List import list_node


def test_cold_find_cycle_fast_slow_ptr() -> None:
    cllc141llcycled28 = ColdLC141LLCycleDay28()
    assert (
        cllc141llcycled28.hasCycle(list_node.build_list([3, 2, 0, -4], pos=1)) is True
    )
    assert cllc141llcycled28.hasCycle(list_node.build_list([1, 2], pos=2)) is False
    assert cllc141llcycled28.hasCycle(list_node.build_list([1, 2, 3], pos=-1)) is False
    assert cllc141llcycled28.hasCycle(list_node.build_list([], pos=0)) is False
    assert cllc141llcycled28.hasCycle(list_node.build_list([3], pos=0)) is True
