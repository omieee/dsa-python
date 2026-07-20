def sortedSquares(nums: list[int]) -> list[int]:
    for i, v in enumerate(nums):
        nums[i] = v**2
    lptr = 0
    rptr = len(nums) - 1
    while lptr < rptr:
        if nums[lptr] < nums[rptr]:
            rptr -= 1
        else:
            tmp = nums[lptr]
            nums[lptr] = nums[rptr]
            nums[rptr] = tmp
            rptr -= 1
    return nums
