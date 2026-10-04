from Closed_Book.cold_delete_nth_from_linked_list import ColdDeleteNth
from Topics_Learning.Linked_List import list_node


def test_delete_nth_from_end() -> None:
    dnfe = ColdDeleteNth()
    assert [1, 2, 3, 5] == list_node.to_list(
        dnfe.deleteNth(list_node.build_list([1, 2, 3, 4, 5]), 2)
    )
    assert [] == list_node.to_list(dnfe.deleteNth(list_node.build_list([1]), 1))

    assert [1] == list_node.to_list(dnfe.deleteNth(list_node.build_list([1, 2]), 1))
