from Closed_Book.cold_LC_739_Daily_TEmp_Day_3 import Cold_LC_739_Daily_TEmp_Day_3


def test_LC_739_Day_1() -> None:
    obj = Cold_LC_739_Daily_TEmp_Day_3()
    assert [1, 4, 1, 2, 1, 0, 0] == obj.clLC739D3([30, 38, 30, 36, 35, 40, 28])
    assert [0, 0, 0] == obj.clLC739D3([22, 21, 20])
    assert [1, 1, 4, 2, 1, 1, 0, 0] == obj.clLC739D3([73, 74, 75, 71, 69, 72, 76, 73])
    assert [2, 1, 0] == obj.clLC739D3([30, 30, 31])
