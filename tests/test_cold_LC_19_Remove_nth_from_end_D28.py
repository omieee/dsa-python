from Closed_Book.cold_LC_19_Remove_nth_from_end_D28 import Cold_LC_19_Remove_Nth_Day_28
from Topics_Learning.Linked_List import list_node


def test_cold_lc19_delete_nth_from_end_d14() -> None:
    clc19d28 = Cold_LC_19_Remove_Nth_Day_28()
    assert [1, 2, 3, 5] == list_node.to_list(
        clc19d28.removeNth(list_node.build_list([1, 2, 3, 4, 5]), 2)
    )
    assert [] == list_node.to_list(clc19d28.removeNth(list_node.build_list([1]), 1))

    assert [1] == list_node.to_list(clc19d28.removeNth(list_node.build_list([1, 2]), 1))

    assert [1, 3, 4] == list_node.to_list(
        clc19d28.removeNth(list_node.build_list([1, 2, 3, 4]), 3)
    )
