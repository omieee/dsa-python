from Topics_Learning.Linked_List import singly_linked_list


def test_add_to_singly_linked_list() -> None:
    ll = singly_linked_list.LinkedList()
    ll.add_node(3)
    ll.add_node(1)
    ll.add_node(5)
    assert [3, 1, 5] == ll.print()


def test_remove_from_singly_linked_list() -> None:
    ll = singly_linked_list.LinkedList()
    ll.add_node(3)
    ll.add_node(1)
    ll.add_node(5)
    ll.delete_at(index=1)
    assert [3, 5] == ll.print()
