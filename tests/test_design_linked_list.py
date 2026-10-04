from Topics_Learning.Linked_List import design_linked_list


def test_empty_ll_returns_none():
    ll = design_linked_list.LinkedList()
    assert None is ll.get(0)


def test_add_item_to_head_when_nothing_is_there():
    ll = design_linked_list.LinkedList()
    ll.add_at_head(12)
    assert 12 == ll.get(0)


def test_add_item_to_tail_when_nothing_is_there():
    ll = design_linked_list.LinkedList()
    ll.add_at_tail(13)
    assert 13 == ll.get(0)


def test_add_item_at_index_when_something_is_there():
    ll = design_linked_list.LinkedList()
    ll.add_at_tail(13)
    ll.add_at_head(12)
    ll.add_at_tail(99)
    ll.add_at_index(212, 2)
    assert 212 == ll.get(2)
    ll.add_at_tail(707)
    ll.add_at_index(97, 0)
    assert 97 == ll.get(0)
    assert [97, 12, 13, 212, 99, 707] == ll.print()


def test_add_at_index_at_end_updates_tail():
    ll = design_linked_list.LinkedList()
    for v in (12, 13, 99):
        ll.add_at_tail(v)
    ll.add_at_index(7, 3)  # index == len -> append, tail must move
    ll.add_at_tail(8)
    assert [12, 13, 99, 7, 8] == ll.print()
