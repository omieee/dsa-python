from Problems.two_sum import two_sum
def test_two_sum():
    nums = [2,7,11,15]
    target = 9

    assert [0,1]  == two_sum(nums=nums, target=target)