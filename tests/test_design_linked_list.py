from Topics_Learning.Linked_List import design_linked_list

# ll = design_linked_list.LinkedList()

# ll.add_at_head(0)
# ll.add_at_tail(1)
# ll.add_at_head(2)
# ll.add_at_tail(3)
# ll.add_at_head(4)
# ll.add_at_head(5)

# ll.print()
# ll.add_at_index(13, 3)
# ll.print()
# ll.add_at_index(11, 0)
# ll.print()
# ll.add_at_index(19, len(ll) - 1)
# ll.print()


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
    ll.add_at_index(97, 0)
    assert 97 == ll.get(0)
    assert [97, 12, 13, 212, 99] == ll.print()
