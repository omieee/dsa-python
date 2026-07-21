# def longest_conseqtive(nums: list[int]) -> list[int]:
#     '''
#     nums = [3,5,6,7,8,1]
#     output = [5,6,7]
#     '''
#     res = set()
#     for i in range(0, len(nums)-1):
#         if nums[i] + 1 == nums[i + 1] and nums[i] - 1 == nums[len(res) - 1]:
#             res.add(nums[i+1])
#             res.add(nums[i])
#     print(res)
#     return len(res)

# # print(longest_conseqtive(nums = [1,2,3,10,11]))


# def longest_consequitive_v2(nums: list[int]) -> int:
#     '''
#     nums = [1,2,3,10,11]
#     output = 3
#     '''

#     lptr = 0
#     rptr = 1
#     longestSeen = {}
#     count = 0
#     if len(nums) > 1:
#         while rptr < len(nums):
#             if nums[lptr] + 1 == nums[rptr]:
#                 if rptr + 1 == len(nums):
#                     longestSeen[count] = nums[lptr:]
#                 rptr += 1
#                 lptr += 1
#             else:
#                 longestSeen[count] = nums[:rptr]
#                 count += 1
#                 lptr += 1
#                 rptr += 1
#     else:
#         pass
#     print(longestSeen)


def longest_consecutive(nums: list[int]) -> int:
    """
    O(n) time, O(n) space.

    Only start counting at sequence starts (n-1 not in set),
    then walk forward with n+1, n+2, ...
    """
    if not nums:
        return 0

    num_set = set(nums)
    print("num_set: ", num_set)
    longest = 0

    for n in num_set:
        # skip if this isn't the start of a sequence
        if n - 1 in num_set:
            continue

        length = 1
        while n + length in num_set:
            length += 1
        longest = max(longest, length)

    return longest
