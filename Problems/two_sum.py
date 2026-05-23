nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
  seen = {}
  for i, v in enumerate(nums):
    need_for = target-v
    if need_for in seen:
      return [seen[need_for], i]
    else:
      seen[v] = i
  return None