class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next: ListNode | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index) -> int | None:
        curr = self.head.next  # Lets start by skipping the first dummy
        i = 1
        while i <= index and curr:
            curr = curr.next
            i += 1
        if curr:
            return curr.val
        else:
            return None

    def add_at_head(self, value):
        new_node = ListNode(value=value)
        nxt = self.head.next  # Pointing at first node
        # only dummy present -> this is effectively add-at-tail, hence else
        if nxt:
            self.head.next = new_node
            new_node.next = nxt
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __len__(self) -> int:
        curr = self.head.next  # Lets start by skipping the first dummy
        length = 0
        while curr:
            curr = curr.next
            length += 1
        return length

    def add_at_index(self, val, index):
        if index > len(self):
            return
        else:
            curr = self.head  # Will be at -1
            i = 0
            while i < index and curr:  # We are seeking to the correct location
                curr = curr.next
                i += 1
            if curr:
                new_node = ListNode(value=val)
                nxt = curr.next
                curr.next = new_node
                new_node.next = nxt

    def add_at_tail(self, value):
        new_node = ListNode(value=value)
        self.tail.next = new_node
        self.tail = new_node

    def delete_at_index(self, index):
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
