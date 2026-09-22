"""Shared linked-list helpers for LeetCode-style problems.

Import this in a solution file and only write the algorithm:

    from Topics_Learning.Linked_List.list_node import ListNode, build_list, to_list

    class Solution:
        def someProblem(self, head: ListNode | None) -> ...:
            ...

    if __name__ == "__main__":
        head = build_list([1, 2, 3])
        print(to_list(Solution().someProblem(head)))
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values: list[int], pos: int = -1) -> ListNode | None:
    """Build a linked list from values.

    pos >= 0 makes the last node point back to index pos (a cycle).
    pos == -1 means no cycle (default).
    """
    if not values:
        return None

    dummy = ListNode()
    curr = dummy
    nodes = []
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)

    if 0 <= pos < len(nodes):
        curr.next = nodes[pos]

    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    """Walk a list and return values. Stops if a cycle is found."""
    out = []
    seen = set()
    curr = head
    while curr:
        if id(curr) in seen:
            break
        seen.add(id(curr))
        out.append(curr.val)
        curr = curr.next
    return out
