"""
Approach:

we will have two pointers  slow and fast. slow starts at head and fast starts one step
ahead. This problem can be solved by thre seprate step
1. find the middle and cut the list in two hald
2. then we wil reverese the second part
3. then we combine both

Time : O(n)
Space: O(1)
"""

from Topics_Learning.Linked_List.list_node import ListNode


class Cold_LC_143_Reorder_List_Day_28:
    def clc143rld28(self, head: ListNode) -> None:
        if head:
            slow, fast = head, head.next
            while fast and fast.next:  # cutting the list here
                slow = slow.next
                fast = fast.next.next
            s = slow.next
            p = slow.next = None
            while s:  # reversing here
                t = s.next
                s.next = p
                p = s
                s = t
            fa, sl = head, p
            while sl:  # mixing here
                t1 = fa.next
                t2 = sl.next
                fa.next = sl
                sl.next = t1
                fa, sl = t1, t2
