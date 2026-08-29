# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseLinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next  # First make sure we capture next item, else will break the
            # link
            curr.next = prev  # Then point the curr to previous
            prev = curr  # Then set the previous to current
            curr = nxt  # Override current with next
            # Basically we are shifting left
        return prev  # pyright: ignore[reportReturnType]
