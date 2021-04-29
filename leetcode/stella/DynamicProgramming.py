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
    # [419, 408, 186, 83]  6249
    rev_coins = sorted(coins, reverse=True)

    def combine(target, choices):
        if not choices or target < min(choices) or (len(choices) == 1 and target % choices[0] != 0):
            return []
        if len(choices) == 2:
            max_left = target % min(choices) % (max(choices)-min(choices))
            if max_left == 0:
                return [[target % min(choices)]]
            else:
                return []

        first_max = int(target / choices[0])
        if target % choices[0] == 0:
            return [[first_max] + [0] * (len(choices) - 1)]
        all_combination = []
        for first_no in range(first_max, -1, -1):
            for c in combine(target - first_no * choices[0], choices[1:]):
                all_combination.append([first_no, *c])
        print(target, choices)
        return all_combination

    all_possibilities = combine(amount, rev_coins)
    return min([sum(poss) if poss else -1 for poss in all_possibilities]) if all_possibilities else -1


if __name__ == '__main__':
    print(coin_change([411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864))
    # print(coin_change([3, 7, 405, 436], 8839))
    # print(coin_change([2], 3))
    # print(coin_change([186, 419, 83, 408], 6249))
