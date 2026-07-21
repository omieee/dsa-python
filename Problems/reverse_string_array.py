def reverseString(s: list[str]) -> list[str]:
    lptr = 0
    rptr = len(s) - 1
    while lptr < rptr:  # that is the mid point
        temp = s[lptr]
        s[lptr] = s[rptr]
        s[rptr] = temp
        lptr += 1
        rptr -= 1
    return s
