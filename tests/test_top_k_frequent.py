from Problems.top_k_frequent import topKFrequent


def test_topKFrequent() -> None:
    assert [1, 2] == topKFrequent([1, 1, 1, 2, 2, 3], k=2)
    assert [1] == topKFrequent([1], k=1)
    assert [7] == topKFrequent([7, 7, 7, 8, 8, 9], k=1)
    assert [4, 5] == topKFrequent([4, 4, 4, 4, 5, 5, 6], k=2)
