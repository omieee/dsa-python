from Closed_Book.cold_LC_739_Daily_Temperature_Day_1 import Cold_LC_739_Daily_Temp_Day_1


def test_LC_739_Day_0() -> None:
    obj = Cold_LC_739_Daily_Temp_Day_1()
    assert [1, 4, 1, 2, 1, 0, 0] == obj.cl79dtd1([30, 38, 30, 36, 35, 40, 28])
    assert [0, 0, 0] == obj.cl79dtd1([22, 21, 20])
