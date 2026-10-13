from Topics_Learning.Linked_List import ListNode

"""
Approach
We will start witha dummy node
and left will be pointing to that and dummy node will point to head
right will point at head, basically a difference of one
then the idea is to bring left one place before the element to be deleted
so we can have that sepration by moving right to n positin
once we have move right by n 
then we will start moving both left and right till right is none
at the end left.next = left.next.next
will return dummy.next

a = [1,2,3,4,5] n = 2

d = dn(-1,head)

l = d
r = 1
move r n times
l = d
r = 3
while r:
    l = left.next
    r = right.next
left.next = left.next.next
dummy.next is returned

Complexity
Time = O(n)
SPace = O(1)
"""


class Cold_LC_19_Delete_Nth_Day_14:
    def deleteNth(self, head: ListNode | None, n: int) -> ListNode | None:
        if head:
            dummy = ListNode(next=head)
            left = dummy
            right = head
            # Now will move right n time, total difference between l and r is n + 1
            while n > 0 and right:
                right = right.next
                n -= 1
            while right:
                left = left.next
                right = right.next
            left.next = left.next.next
            return dummy.next
        else:
            return None
