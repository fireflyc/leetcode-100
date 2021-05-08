from typing import List


def house_robber(houses: List[int]) -> int:
    l = len(houses)
    max1, max2 = houses[0], max(houses[0], houses[1] if l > 1 else 0)
    maxn = max(max1, max2)
    for idx in range(2, l):
        tmp1 = max1 + houses[idx]
        maxn = max(tmp1, max2)
        max1, max2 = max2, maxn
    return maxn


def coin_change(coins: List[int], amount: int) -> int:
    cache = {}

    def change(target):
        if target in cache:
            return cache[target]
        dp = -1
        if target == 0:
            return 0
        if target < 0:
            return -1
        if target in coins:
            return 1
        for cdp in [change(target-coin) for coin in coins]:
            if cdp > -1:
                dp = cdp+1 if dp == -1 else min(dp, cdp+1)
        cache[target] = dp
        return dp

    return change(amount)

