from Closed_Book.cold_reverse_ll import ReverseLinkedList
from Topics_Learning.Linked_List.list_node import ListNode


def as_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def test_reverse_linked_list() -> None:
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    rll = ReverseLinkedList()
    assert as_list(rll.rL(head=l1)) == [3, 2, 1]
    assert as_list(rll.rL(head=None)) == []
    assert as_list(rll.rL(head=ListNode(1))) == [1]
