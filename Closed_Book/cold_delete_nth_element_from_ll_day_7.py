from Topics_Learning.Linked_List import ListNode

"""
Approach:
Will create a dummy node so that our left pointer can start from there
then seek right to n steps so that there is a difference of n always in between
then move both left and right till right reaches last
left will; be at a position just before deleting
will skip left.next by one step left.next.next
"""

"""
Complexity:
TIme: O(n) the whole list is traverserd once
Space: O(1)
"""


class ColdClosedDeleteNth:
    def deleteNth(self, head: ListNode | None, n: int) -> ListNode | None:
        if head:
            dummy = ListNode(next=head)
            slow = dummy
            fast = head

            while n > 0 and fast:
                fast = fast.next
                n -= 1

            while fast:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            return dummy.next
