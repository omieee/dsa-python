from Topics_Learning.Linked_List.list_node import ListNode


class ReverseLinkedList:
    def rL(self, head: ListNode | None) -> ListNode | None:
        pre, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre
