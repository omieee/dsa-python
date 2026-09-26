from Topics_Learning.Linked_List.list_node import ListNode


class ReverseLinkedList:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head

        while curr:
            nxt = curr.next  # First make sure we capture next item, else will break the
            # link
            curr.next = prev  # Then point the curr to previous
            prev = curr  # Then set the previous to current
            curr = nxt  # Override current with next
            # Basically we are shifting left
        return prev
