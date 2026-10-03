from Topics_Learning.Linked_List.list_node import ListNode


class CheckCycle:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head:
            left = head
            right = head.next

            while right:
                if right == left:
                    return True
                else:
                    if right.next:
                        right = right.next.next
                        left = left.next
                    else:
                        return False

        return False
