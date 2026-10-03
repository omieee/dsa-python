from Topics_Learning.Linked_List import ListNode

"""
Approach:
Will create a dummy node so that our left pointer can start from there
then seek right to n steps so that there is a difference of n+1 always in between
then move both left and right till right reaches last means right is at None
left will; be at a position just before deleting
will skip left.next by one step left.next.next

flow:
step 1:
slow at dummy pointing next to -> head
fast at head
when n = 2
slow at dummy
fast at 3
when loop ends
fast is at 3 then:
slow is at 1, fast is at 4
slow is at 2, fast is at 5
slow is at 3, fast is at none
Loop ends
slow.next = slow.next.next
which makes slow.next point to 5 .. fuck 4

"""

"""
Complexity:
TIme: O(L) the whole list is traverserd once
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
