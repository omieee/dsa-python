from Topics_Learning.Stacks.LC_739_Daily_Temperatures import LC_739_Daily_Temp_Day_0


def test_LC_739_Day_0() -> None:
    obj = LC_739_Daily_Temp_Day_0()
    assert [1, 4, 1, 2, 1, 0, 0] == obj.DailyTemperatures([30, 38, 30, 36, 35, 40, 28])
    assert [0, 0, 0] == obj.DailyTemperatures([22, 21, 20])
