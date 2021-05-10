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
        for cdp in [change(target - coin) for coin in coins]:
            if cdp > -1:
                dp = cdp + 1 if dp == -1 else min(dp, cdp + 1)
        cache[target] = dp
        return dp

    return change(amount)


def coin_change2(coins: List[int], amount: int) -> int:
    coins = sorted(coins, reverse=True)
    cache = {}

    def change(choices, target):
        if target in cache and len(choices) in cache[target]:
            return cache[target][len(choices)]
        makeup = 0
        if target <= 0:
            return makeup
        if target in choices:
            makeup += 1
        for i, v in enumerate(choices):
            makeup += change(choices[i:], target - v)
        cache[target] = cache.get(target) or {}
        cache[target][len(choices)] = makeup
        return makeup

    return change(coins, amount) if amount > 0 else 1


def length_of_lts(nums: List[int]) -> int:
    cache = []
    while nums:
        last = nums.pop()
        _cache = [last]
        for c in cache:
            if last + 1 == c[0]:
                cache.remove(c)
            if last < c[0] and len(c) + 1 > len(_cache):
                _cache = [last] + c
        cache.append(_cache)

    return max([len(c) for c in cache])


def min_cost_tickets(days: List[int], costs: List[int]) -> int:
    day_cost = {1: costs[0], 7: costs[1], 30: costs[2]}
    cache = {}

    def cost(period):
        payment = 0
        if not period:
            return 0
        if period[0] in cache:
            return cache[period[0]]
        for d, c in day_cost.items():
            left_cost = cost([p for p in period if p > period[0] + d - 1]) + c
            payment = min(left_cost, payment) if payment else left_cost
        cache[period[0]] = payment
        return payment

    return cost(days)


def unique_binary_search_trees(n: int) -> int:
    cache = {}

    def tree(nodes: list):
        amount = 0
        if len(nodes) <= 0:
            return 1
        if len(nodes) in cache:
            return cache[len(nodes)]
        for i in range(0, len(nodes)):
            left_tree = tree(nodes[:i])
            right_tree = tree(nodes[i+1:])
            amount += left_tree * right_tree
        cache[len(nodes)] = amount
        return amount

    return tree(list(range(0, n)))


def trapping_rain_water(height: List[int]) -> int:
    amount = 0
    for i, h in enumerate(height):
        min_height = min(max(height[:i] or [0]), max(height[i+1:] or [0]))
        if min_height > h:
            amount += min_height-h
    return amount


def edit_distance(word1: str, word2: str) -> int:
    cache = {}

    def edit(w1, w2):
        if not w1 or not w2:
            return max(len(w2), len(w1))
        if w1[-1] == w2[-1]:
            return edit(w1[:-1], w2[:-1])
        if w2 in cache and w1 in cache[w2]:
            return cache[w2][w1]
        min_distance = min([1 + edit(w1, w2[:-1]), 1 + edit(w1[:-1], w2), 1 + edit(w1[:-1], w2[:-1])])
        cache[w2] = cache.get(w2) or {}
        cache[w2][w1] = min_distance
        return min_distance

    return edit(word1, word2)

