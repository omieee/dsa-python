from Topics_Learning.Stacks.baseball_game import BaseBallCalculation


def test_baseball_claculations() -> None:
    bbc = BaseBallCalculation()
    assert 18 == bbc.calPoints(["1", "2", "+", "C", "5", "D"])
    assert 15 == bbc.calPoints(["5", "D", "+", "C"])
