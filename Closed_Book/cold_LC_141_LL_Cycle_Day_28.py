from Topics_Learning.Linked_List.list_node import ListNode

"""
Approach:
two pointer one fast one slow
when fast starts one step ahead and then fast moves 2 steps at a time
until it is none. and slow will move by one position.
if at any point fat and sloww meets.. means we havea cycle

Complextiy:
Time: O(n)
Space: O(1)
"""


class ColdLC141LLCycleDay28:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head:
            slow = head
            fast = head.next

            while fast:
                if fast == slow:
                    return True
                else:
                    if fast.next:
                        fast = fast.next.next
                        slow = slow.next
                    else:
                        return False
            return False
        else:
            return False
