def sortedSquares(nums: list[int]) -> list[int]:
    lptr = 0
    rptr = len(nums) - 1
    output = []  # Will store the result here
    """
    So the idea is if the input is a sorted array the largest squares will be at the
    either end on left side worst case will be biggest negative number and on right
    side will be the biggest positive number.. the both can produce squares
    [-4,-3,-2,-1,0,5,6,7,8] will give [16,9,4,1,0,25,36,49,64]
    We can see the valley forming first decrease to lowe number and then increases
    And because the input were already sorted means left side will ---> decrease to near
    0 and right side will <--- decrease this way

    Based on above intuition we can do like this let say input is [-2,-1,3,4]
    Iteration 1: Is (-2 ** 2) > (4 ** 2) [NO]:
                 output.append(16) and rptr decrease by 1
    Iteration 2: Is (-2 ** 2) > (3 ** 2) [NO]:
                 output.append(9) and rptr decrease by 1
    Iteration 3: Is (-2 ** 2) > (-1 ** 2) [YES]:
                 output.append(4) and lptr increase by 1
    Iteration 4: Is (-1 ** 2) > (-1 ** 2) [NO]: BOTH ARE POINTING CURRENTLY TO SAME
                 output.append(2) and rptr decrease by 1
    Iteration 5: won't happen because lptr = 1 and rptr is now 0

    At this point output list is = [16,9,4,2]. But we are asked to return sorted so
    return output[::-1] Basically return everything in reverse
    
    """
    while lptr <= rptr:
        if nums[lptr] ** 2 > nums[rptr] ** 2:
            output.append(nums[lptr] ** 2)
            lptr += 1
        else:
            output.append(nums[rptr] ** 2)
            rptr -= 1
    return output[::-1]
