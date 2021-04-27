from typing import List


def house_robber(houses: List[int]) -> int:
    if len(houses) == 1:
        return houses[0]
    if not houses:
        return 0
    return max(houses[0] + house_robber(houses[2:]), houses[1] + house_robber(houses[3:]))
