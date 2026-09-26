from Topics_Learning.Linked_List import list_node
from Topics_Learning.Linked_List.reorder_list import ReorderList


def test_reorder_list() -> None:
    s = ReorderList()
    head = list_node.build_list([1, 2, 3, 4])
    s.reorderList(head)
    assert list_node.to_list(head) == [1, 4, 2, 3]

    head = list_node.build_list([1, 2, 3, 4, 5])
    s.reorderList(head)
    assert list_node.to_list(head) == [1, 5, 2, 4, 3]

    head = list_node.build_list([1, 2])
    s.reorderList(head)
    assert list_node.to_list(head) == [1, 2]

    head = list_node.build_list([1])
    s.reorderList(head)
    assert list_node.to_list(head) == [1]
