from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    seen = defaultdict(int)

    for n in nums:
        seen[n] += 1

    """
    Now we have got the count of each
    We will sort the dictionary based on frequency in decressing order 
    and atlast will return top k values (frequency)
    """

    sorted_thing = sorted(seen.items(), key=lambda pair: pair[1], reverse=True)
    return [pair[0] for pair in sorted_thing[:k]]
