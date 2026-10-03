from Topics_Learning.Linked_List import ListNode


class ColdDeleteNth:
    def deleteNth(self, head: ListNode | None, n: int) -> ListNode | None:
        if head:
            dummynode = ListNode(-1, head)
            left = dummynode
            right = head
            # for right we will seek till that number
            while n > 0 and right:
                right = right.next
                n -= 1
            while right:
                left = left.next
                right = right.next
            left.next = left.next.next
            return dummynode.next
