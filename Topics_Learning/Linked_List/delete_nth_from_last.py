from Topics_Learning.Linked_List.list_node import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class DeleteNthFromEnd:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # I don't know the size of LL
        # else what i would have done is
        # delIndex = size - (n + 1) that element is
        # to be removed and the previous's tail from delIndex
        # should be connnected to next's head from delIndex
        if head:
            dummy = ListNode(-1, head)
            left = dummy
            right = head
            # while n > 0 and right:
            #     right = right.next
            #     n -= 1
            for _ in range(n):
                if right:
                    right = right.next
            while right:
                left = left.next
                right = right.next
            left.next = left.next.next
            return dummy.next
