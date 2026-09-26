from Topics_Learning.Linked_List.list_node import ListNode


class FindCycleBruteForce:
    def hasCycle(self, head: ListNode | None) -> bool:
        if head:
            # This shoul be the brute force way of doing it
            # where we have a seen dictionary that will add
            # up to the most O(n) space and time is O(n)
            # seen = {} # This would have made is O(n^2)
            seen = set()  # O(n)
            curr = head.next
            while curr:
                if curr in seen:
                    return True
                else:
                    seen.add(curr)
                    curr = curr.next
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
