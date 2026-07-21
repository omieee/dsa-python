"""
Input: s = "Was it a car or a cat I saw?"

Output: true

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

Dry Run:
Palindrome means a string if reversed is same as original string

So we can have two pinter one pointing to left end and the other to the
right end. and we will move lift one pos right and right to one pos left
we will continue till half way from both side

If each time the character is same we can call it palindrome
"""


def cold_is_palindrome(stri: str) -> bool:
    lptr = 0
    rptr = len(stri) - 1

    while lptr < rptr:
        if stri[lptr].isalnum():
            if stri[rptr].isalnum():
                if stri[lptr].lower() == stri[rptr].lower():
                    lptr += 1
                    rptr -= 1
                else:
                    return False
            else:
                rptr -= 1
        else:
            lptr += 1
    return True


# print(cold_is_palindrome("Was it a car or a cat I saw?"))
# print(cold_is_palindrome("Was it a cart or a cat I saw?"))
