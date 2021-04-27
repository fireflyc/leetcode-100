from typing import List


def solution(houses: List[int]) -> int:
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
