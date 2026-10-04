from Closed_Book.cold_delete_nth_element_from_ll_day_7 import ColdClosedDeleteNth
from Topics_Learning.Linked_List import list_node


def test_delete_nth_from_last() -> None:
    ccdn = ColdClosedDeleteNth()
    assert [1, 2, 3, 5] == list_node.to_list(
        ccdn.deleteNth(list_node.build_list([1, 2, 3, 4, 5]), 2)
    )
    assert [] == list_node.to_list(ccdn.deleteNth(list_node.build_list([1]), 1))

    assert [1] == list_node.to_list(ccdn.deleteNth(list_node.build_list([1, 2]), 1))
