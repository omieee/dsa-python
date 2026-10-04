from Topics_Learning.Linked_List import ListNode


class ColdMergeTwoSorted:
    def mTL(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
        return dummy.next
