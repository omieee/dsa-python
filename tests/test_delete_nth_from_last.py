from Topics_Learning.Linked_List import list_node
from Topics_Learning.Linked_List.delete_nth_from_last import DeleteNthFromEnd


def test_delete_nth_from_end() -> None:
    dnfe = DeleteNthFromEnd()
    assert [1, 2, 3, 5] == list_node.to_list(
        dnfe.removeNthFromEnd(list_node.build_list([1, 2, 3, 4, 5]), 2)
    )
    assert [] == list_node.to_list(dnfe.removeNthFromEnd(list_node.build_list([1]), 1))

    assert [1] == list_node.to_list(
        dnfe.removeNthFromEnd(list_node.build_list([1, 2]), 1)
    )
