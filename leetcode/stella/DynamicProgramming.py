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


def maximize_profit(prices: List[int]) -> int:
    # best_time_to_buy_and_sell_stock
    if len(prices) <= 1:
        return 0
    max_profit = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        sell = prices[i]
        if sell > buy:
            max_profit = max(max_profit, sell-buy)
        elif sell < buy:
            buy = sell
    return max_profit


def maximize_profit2(prices: List[int]) -> int:
    if len(prices) <= 1:
        return 0
    max_profit = 0
    for i in range(0, len(prices)-1):
        profit = prices[i+1] - prices[i]
        if profit > 0:
            max_profit += profit
    return max_profit


def maximize_profit3(prices: List[int]) -> int:
    begin, end = [], []
    begin_min, end_max = prices[0], prices[-1]
    for i in range(0, len(prices)):
        begin_pre = begin[i-1] if begin else 0
        begin.append(max(begin_pre, prices[i] - begin_min))
        begin_min = min(begin_min, prices[i])

        end_idx = -1*(i+1)
        end_next = end[-1] if end else 0
        end.append(max(end_max - prices[end_idx], end_next))
        end_max = max(end_max, prices[end_idx])

    return max([begin[i]+end[-1*(i+1)] for i in range(0, len(begin))])


def super_egg_drop(k: int, n: int) -> int:
    cache = {}

    def drop_egg(eggs, floors):
        if eggs == 1 or floors <= 2:
            return floors
        if floors in cache and eggs in cache[floors]:
            return cache[floors][eggs]

        min_drop = 0
        start, end = 1, floors
        while end > start + 1:
            middle = int((start + end) / 2)
            left, right = drop_egg(eggs-1, middle-1), drop_egg(eggs, floors-middle)
            drop = 1 + max(left, right)
            min_drop = min(min_drop, drop) if min_drop > 0 else drop
            start, end = (middle, end) if right > left else (start, middle)

        cache[floors] = cache.get(floors) or {}
        cache[floors][eggs] = min_drop
        return min_drop

    return drop_egg(k, n)


def maximal_square(matrix: List[List[str]]) -> int:
    cache = {}

    def side(r, c):
        if r >= len(matrix) or c >= len(matrix[r]):
            return 0
        if r in cache and c in cache[r]:
            return cache[r][c]
        if matrix[r][c] == '1':
            s = 1 + min(side(r, c+1), side(r+1, c), side(r+1, c+1))
            cache[r] = cache.get(r) or {}
            cache[r][c] = s
            return s
        return 0

    largest = 0
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[r])):
            largest = max(side(r, c), largest)

    return largest*largest


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    count, subarray_sum = 0, 0
    cache = {k: 1}
    for i in range(0, len(nums)):
        subarray_sum += nums[i]
        count += (cache.get(subarray_sum) or 0)
        num_plus_k = subarray_sum + k
        cache[num_plus_k] = (cache.get(num_plus_k) or 0) + 1
    return count




