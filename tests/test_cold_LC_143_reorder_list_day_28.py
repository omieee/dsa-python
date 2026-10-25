from Closed_Book.cold_LC_143_reorder_list_day_28 import Cold_LC_143_Reorder_List_Day_28
from Topics_Learning.Linked_List import list_node


def test_reorder_list() -> None:
    s = Cold_LC_143_Reorder_List_Day_28()
    head = list_node.build_list([1, 2])
    s.clc143rld28(head)
    assert list_node.to_list(head) == [1, 2]

    head = list_node.build_list([1])
    s.clc143rld28(head)
    assert list_node.to_list(head) == [1]

    head = list_node.build_list([1, 2, 3, 4])
    s.clc143rld28(head)
    assert list_node.to_list(head) == [1, 4, 2, 3]

    head = list_node.build_list([1, 2, 3, 4, 5])
    s.clc143rld28(head)
    assert list_node.to_list(head) == [1, 5, 2, 4, 3]
