from Topics_Learning.Linked_List.list_node import ListNode


class FindCycleBruteForce:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head:
            # This shoul be the brute force way of doing it
            # where we have a seen dictionary that will add
            # up to the most O(n) space and time is O(n)
            seen = {}  # O(n)
            count = 1
            curr = head.next
            while curr:
                if curr in seen.values():
                    return True
                else:
                    seen[count] = curr
                    curr = curr.next
                    count += 1
        return False


class FindCycleSlowFastPtr:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head:
            sl_ptr = head
            fa_ptr = head.next  # Will start with next in list

            while fa_ptr:
                if sl_ptr is fa_ptr:
                    return True
                else:
                    if fa_ptr.next:
                        fa_ptr = fa_ptr.next.next  # Floyd's algo 2 steps at a time
                        sl_ptr = sl_ptr.next
                    else:
                        return False
        return False
