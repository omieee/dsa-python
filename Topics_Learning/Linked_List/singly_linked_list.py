"""
There are two things here:
1.  ListNode: It is the single node of a long linked list. It has a value and a next
    that points to the next Listnode

2.  LinkedList: This is a chain of ListNodes where each node has some value and next
    nodes location
"""


class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next: ListNode | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head

    def add_node(self, value):
        new_node = ListNode(value=value)
        self.tail.next = new_node
        self.tail = new_node

    def delete_at(self, index):
        curr = self.head  # Will be at -1
        i = 0
        while i < index and curr:  # We are seeking to the correct location
            curr = curr.next
            i += 1
        if curr and curr.next:  # curr exist and there is a node to delete
            if curr.next is self.tail:  # Will the deleted node be the last node
                # So the end will get removed,so the current should now be made the tail
                self.tail = curr  # Setting current as final, next line deletes next
            curr.next = curr.next.next  # We are mapping seconnd next to current next

    def print(self) -> list:  # Just returning so that test cases is easy
        curr = self.head.next  # Skip dummy
        out = []
        while curr:
            print(curr.val, " -> ", end="")
            out.append(curr.val)
            curr = curr.next
        print()
        return out
