from Topics_Learning.Linked_List import ListNode

"""
Approach: So the idea is to have two pointers and position the left pointer
just before the item to be deleted that is (nth pos from end including end)
To achieve that we need to seek left pointer 
So we want left pointer to start 1 step back of r poiter and to achieve that we will
create a dummy node that will point to head and assign that dummy node to lptr adn
the rptr will start from head. first we need a separation on n numbers + 1 
between both pointer that 1 is achieved by adding dummy node and then the remaing n
will be acieved by only seeking rptr to n positions soa total of n+1 pos gap is there
Now the second loop will be till rptr is not None we will move both pointer 1-1
position. At the end of loop we will break the lptr's next and move it to next.next
and return the dummy.next because we don't want the extra styarting dummy node

Complexity:
O(N): As we are looping throul ll only once
O(1): Nothing much extra space is required
"""


class Cold_LC_19_Remove_Nth_Day_28:
    def removeNth(self, head: ListNode | None, n: int) -> ListNode | None:
        if head:
            dummy = ListNode(-1, next=head)
            lptr = dummy
            rptr = head
            while rptr and n > 0:
                rptr = rptr.next
                n -= 1
            while rptr:
                lptr = lptr.next
                rptr = rptr.next
            lptr.next = lptr.next.next
            return dummy.next
        return None
