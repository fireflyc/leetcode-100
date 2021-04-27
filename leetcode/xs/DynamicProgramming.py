from typing import List


def house_robber(houses: List[int]) -> int:
    """
        https://leetcode-cn.com/problems/house-robber/
        思路：对于任意一个序列，不相邻只有两种取法。
        如[2, 4, 1, 5, 3]，取2+1+3=6，取4+5=9，那么取两种方法中最大的即为所求结果
        :param houses:
        :return:
        """
    sum_a = 0  # 取法1
    sum_b = 0  # 取法2
    for i in range(0, len(houses)):
        if i % 2 == 0:
            sum_a += houses[i]
        else:
            sum_b += houses[i]
    return max(sum_a, sum_b)


def fib(n: int) -> int:
    """
    求第n个斐波那契数列
    思路：不要用递归，容易想到的方案是设
    a=1,  b=1, 那么循环 3-n，依次用a=b， b=b+a。把两个变量想象成两个指针，依次移动两个指针的位置
    :param n:
    :return:
    """
    a = 1
    b = 1
    if n <= 2:
        return 1
    for i in range(3, n + 1):
        t = b  # 暂存b
        b = a + b
        a = t
    return b


def coin_change(coins: List[int], amount: int) -> int:
    """
    https://leetcode-cn.com/problems/coin-change/
    思路：不停的寻找"最大"的
    :return:
    """
    order_coins = sorted(coins)
    remain = amount
    max_coin_idx = len(order_coins) - 1  # 最大的硬币所在下标
    count = 0
    while remain > 0:
        if max_coin_idx < 0:
            return -1
        t = remain - order_coins[max_coin_idx]
        if t < 0:
            max_coin_idx -= 1
        else:
            remain = t
            count += 1

    return count


def coin_change2():
    """
    https://leetcode-cn.com/problems/coin-change-2/
    :return:
    """
    return 0
