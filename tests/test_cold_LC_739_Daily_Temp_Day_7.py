from Closed_Book.cold_LC_739_daily_temp_day_7 import Cold_LC_739_Daily_Temp_Day_7


def test_LC_739_Day_7() -> None:
    obj = Cold_LC_739_Daily_Temp_Day_7()
    assert [1, 4, 1, 2, 1, 0, 0] == obj.clc739dtd7([30, 38, 30, 36, 35, 40, 28])
    assert [0, 0, 0] == obj.clc739dtd7([22, 21, 20])
    assert [1, 1, 4, 2, 1, 1, 0, 0] == obj.clc739dtd7([73, 74, 75, 71, 69, 72, 76, 73])
    assert [2, 1, 0] == obj.clc739dtd7([30, 30, 31])
