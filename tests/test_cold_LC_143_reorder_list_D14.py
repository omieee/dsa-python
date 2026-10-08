from Closed_Book.cold_LC_143_reorder_list_day_14 import Cold_LC_143_D14
from Topics_Learning.Linked_List import list_node


def test_reorder_list() -> None:
    s = Cold_LC_143_D14()
    head = list_node.build_list([1, 2])
    s.rerderList(head)
    assert list_node.to_list(head) == [1, 2]

    head = list_node.build_list([1])
    s.rerderList(head)
    assert list_node.to_list(head) == [1]

    head = list_node.build_list([1, 2, 3, 4])
    s.rerderList(head)
    assert list_node.to_list(head) == [1, 4, 2, 3]

    head = list_node.build_list([1, 2, 3, 4, 5])
    s.rerderList(head)
    assert list_node.to_list(head) == [1, 5, 2, 4, 3]
