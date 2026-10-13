from Topics_Learning.Linked_List.list_node import ListNode

"""
Approach:

Frist I take two pointr, slow and fast. Slow moove 1 step, fast moove 2 step.
Wen fast reech the end, slow is in midle.

Then I cut the list from midle. Frist half stay same. Secnd half I keep in sec.

Then I revers the secnd half. So last node come in frunt.

Then I merg both list. Take one node from frist, one node from secnd, agen one
from frist, one from secnd, like this untill secnd half finsh.

Complexity:
Time : O(n)
Space: O(1)
"""


class Cold_LC_143_D14:
    def rerderList(self, head: ListNode) -> None:
        if head:
            slow, fast = head, head.next

            # Part 1: find the middle and split
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            sec = slow.next
            pre = slow.next = None

            # Part 2: Reverse the second part
            while sec:
                tmp = sec.next
                sec.next = pre
                pre = sec
                sec = tmp

            f, s = head, pre

            # Part 3: Combine both
            while s:
                t1 = f.next
                t2 = s.next
                f.next = s
                s.next = t1
                f, s = t1, t2
