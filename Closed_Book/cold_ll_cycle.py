from Topics_Learning.Linked_List.list_node import ListNode


class CheckCycle:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head:  # will make sure None and [] are taken care
            slow = head
            fast = head.next
            while fast:
                if slow == fast:
                    return True
                else:
                    if fast.next:
                        slow = slow.next
                        fast = fast.next.next
                    else:
                        return False
        return False
