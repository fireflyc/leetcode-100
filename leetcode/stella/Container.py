
from typing import List


def count_triplets(nums: List[int]) -> int:
    tuples = {}
    for m in nums:
        for n in nums:
            nm = n & m
            tuples[nm] = tuples.get(nm) or 0
            tuples[nm] += 1
    count = 0
    for n in nums:
        for k in tuples:
            if n & k == 0:
                count += tuples[k]
    return count

