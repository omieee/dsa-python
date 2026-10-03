from Topics_Learning.Linked_List.list_node import ListNode


class ReorderList:
    def reorderList(self, head: ListNode | None) -> None:
        slow = fast = head  # Both points to head
        while fast.next and fast.next.next:  # Check if past can move 2 pos
            slow = slow.next  # Slow moves by 1
            fast = fast.next.next  # Fast moves by 2
        second_half = slow.next  # Thats the starting of second half
        slow.next = None  # Cutting the slow one here coz we got sewcond half
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
