# Start: 11:10 AM
import math


class Cold_LC_875_Koko_Eating_Banana_Day_7:
    def slowestgPossible(self, stack: list[int], h: int) -> int:
        # First we have to find the range what is the minimum required speed to eat
        # banana and fastest posible speed in which he can finish
        # slowest is ofcource 1 because anything less than 1 either he is not eating
        # or vomiting and fastest is the max stack he has because any thing lower will
        # also fisniosh he he eats at that speed
        sl, fa = 1, max(stack)  # so the minimum possible speed is within this range and
        # both inclusive
        # to start with at this speed definately all wil finish
        speed = fa
        while sl <= fa:
            m = (sl + fa) // 2
            # now lets calculate he koko eats at "m" speed how much time it takes him
            #  to finsish all
            ho = 0
            for s in stack:
                ho += math.ceil(s / m)
            # now lets see if koko at given "m" speed is slow or fast and move our searc
            #  accordingl;y
            if ho <= h:
                # koko can eat faster
                speed = min(speed, m)
                fa = m - 1
            else:
                sl = m + 1
        return speed
