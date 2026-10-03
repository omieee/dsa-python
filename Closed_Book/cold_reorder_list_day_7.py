from Topics_Learning.Linked_List.list_node import ListNode

"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]


Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000


HOW I WILL SOLVE IT:

we can have three situations
empty list (evnthough thew above constraint says it will not), 
even count list or odd count list

so if empty list nothing to do 

now lets break down 
l1 = [1,2,3,4]
so steps should be
1. find the mid point
2. break it into two
3. reverse the second one
4. merge both together

"""


class ReorderList:
    def reorderList(self, head: ListNode | None) -> None:
        if head:
            # Lets try to break
            left = right = head
            while right.next and right.next.next:
                left = left.next
                right = right.next.next
            # We have reached, now left should be at the center so teh second half start
            #  from lkeft.next now will keep that in avariable
            second_half = left.next
            left.next = (
                None  # as we stored the second half above we can cut the left side now
            )
            new_head = None
            while second_half:  # Will reverse the second half
                next = second_half.next
                second_half.next = new_head
                new_head = second_half
                second_half = next
            first = head
            second = new_head

            while first and second:
                t1 = first.next
                t2 = second.next
                first.next = second
                second.next = t1
                first = t1
                second = t2
