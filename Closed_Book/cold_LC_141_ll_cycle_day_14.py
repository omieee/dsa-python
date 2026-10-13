from Topics_Learning.Linked_List.list_node import ListNode

"""
Approach:
we will use two pointers one fast one slow 
fast starts one step ahead of slow
fast moves by 2 position till it not none, slow moves one
if at any place fast and slow points to same we can say we have a cycle

Complextiy:
Time: O(n)
Space: O(1)
"""


class ColdLLCycleD14:
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
