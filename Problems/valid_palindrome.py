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

Ex if:
s = "cat tac?"
Then:
1:  l = 0 r = 8-1 = 7
2:  until l < r we will
3:      check if char[l] char[r] is alphanumeric in two separate if
            if both are alphanum then will check both are same char
                we will increase l by 1 and decrease r by 1
            else
                if char is different than it's not a palindrome return False
        else char[r] is not alphanum we will decrease r by 1
        else char[l] is not alphanum we will increase r by 1
    return True, it it reached here

Big O Notations:
    Time Complexity: O(n) as we are looping one time
    Space Complexity: O(1) no significant extra datastructures used
"""


def is_palindrome(stri: str) -> bool:
    le = 0
    ri = len(stri) - 1

    while le < ri:
        if stri[le].isalnum():
            if stri[ri].isalnum():
                if stri[le].lower() == stri[ri].lower():
                    le += 1
                    ri -= 1
                else:
                    return False
            else:
                ri -= 1
        else:
            le += 1
    return True
