from Topics_Learning.Linked_List.merge_two_sorted_list import ListNode, Solution


def build(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def as_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def test_both_non_empty_interleaves():
    got = Solution().mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))
    assert [1, 1, 2, 3, 4, 4] == as_list(got)


def test_first_empty_returns_second():
    assert [0] == as_list(Solution().mergeTwoLists(None, build([0])))


def test_second_empty_returns_first():
    assert [5, 9] == as_list(Solution().mergeTwoLists(build([5, 9]), None))


def test_both_empty_returns_none():
    assert Solution().mergeTwoLists(None, None) is None


def test_one_list_exhausted_mid_merge_tail_attaches():
    got = Solution().mergeTwoLists(build([1, 2]), build([3, 4, 5, 6]))
    assert [1, 2, 3, 4, 5, 6] == as_list(got)


def test_all_equal_values_keeps_every_node():
    got = Solution().mergeTwoLists(build([2, 2]), build([2, 2]))
    assert [2, 2, 2, 2] == as_list(got)


def test_no_new_nodes_allocated_original_nodes_are_relinked():
    a, b = build([1]), build([2])
    got = Solution().mergeTwoLists(a, b)
    assert got is a and got.next is b
