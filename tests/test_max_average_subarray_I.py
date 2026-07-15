import pytest
from Problems.max_average_subarray_I import Solution


@pytest.fixture
def solution():
    return Solution()


def test_findMaxAverage(solution):
    assert solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert solution.findMaxAverage([5], 1) == 5.0
    assert solution.findMaxAverage([-1], 1) == -1.0
    assert solution.findMaxAverage([0, 0, 0, 0, 0], 1) == 0.0
    assert solution.findMaxAverage([1, 1, 1, 1, 1], 3) == 1.0
    assert solution.findMaxAverage([1, 1, 1, 1, 1], 4) == 1.0
    assert solution.findMaxAverage([1, 1, 1, 1, 1], 5) == 1.0
