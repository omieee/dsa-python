from Topics_Learning.Linked_List.reverse_linked_list import ListNode, ReverseLinkedList


def test_reverse_linked_list() -> None:
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    rll = ReverseLinkedList()
    assert 3 == rll.reverseList(head=l1).val
