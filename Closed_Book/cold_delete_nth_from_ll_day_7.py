from Topics_Learning.Linked_List.list_node import ListNode

"""
Given the head of a linked list, remove the nth node from the end of the list and return
its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""


"""
Approach:
first we wqill make sure there is something in head to delete.. if nothing return None
now as the return needs a Listnode we will create a dummynode
and the l pointer can refer that 
and make right pointer to head (conceptually)
will first seek the right pointer to the position equal to n steps
So basically we have to create a gap on n between both pointers so always 
when right is at end and right.next is none left will always be one before the element
to be deleted
so now we can start moving left till there is right
once right comes to an end left will be n+1 position
we will set left.next to left.next.next
then return dummynode next value as the start value is anyways invalid 
"""
"""
Complexity:
Time: O(n) : even though two while but at the end it runs only once
Space: O(1)
"""


class CDN:
    def delNth(self, head: ListNode | None, n: int) -> ListNode | None:
        if head:
            dn = ListNode(-1, head)
            lft = dn
            rgt = head
            while n > 0 and rgt:
                rgt = rgt.next
                n -= 1
            while rgt:
                lft = lft.next
                rgt = rgt.next
            lft.next = lft.next.next
            return dn.next
