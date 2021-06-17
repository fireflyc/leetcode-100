from typing import List


def find_the_distance_value_between_two_arrays(arr1: List[int], arr2: List[int], d: int) -> int:
    total = len(arr1)
    for n1 in arr1:
        for n2 in arr2:
            if abs(n1 - n2) <= d:
                total -= 1
                break
    return total


def rotate_matrix_lcci(matrix: List[List[int]]) -> None:
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0, len(matrix)):
        for j in range(0, int(len(matrix[0]) / 2)):
            matrix[i][j], matrix[i][len(matrix[0]) - 1 - j] = matrix[i][len(matrix[0]) - 1 - j], matrix[i][j]


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    def merge(l1, l2):
        if l1[1] < l2[0] or l2[1] < l1[0]:
            return None
        return [min(l1[0], l2[0]), max(l1[1], l2[1])]

    total_len = len(intervals)
    for i in range(0, total_len):
        if intervals[i] is not None:
            for j in range(0, total_len):
                if j != i and intervals[j]:
                    m = merge(intervals[i], intervals[j])
                    if m:
                        intervals[j] = m
                        intervals[i] = None
                        break
    return [i for i in intervals if i is not None]


def jump_game(nums: List[int]) -> bool:
    reachable, gap = True, 1
    for i in range(len(nums)-2, -1, -1):
        if nums[i] >= gap:
            reachable = True
            gap = 1
        if nums[i] == 0 or (nums[i] < gap and not reachable):
            reachable = False
            gap += 1
    return reachable


def container_with_most_water(height: List[int]) -> int:
    most_water = 0
    start, end, loop = 0, len(height)-1, True
    while start < end and loop:
        loop = False
        most_water = max(min(height[start], height[end])*(end-start), most_water)
        if height[start] >= height[end]:
            for i in range(end-1, start, -1):
                if height[i] > height[end]:
                    end = i
                    loop = True
                    break
        elif height[end] > height[start]:
            for i in range(start+1, end):
                if height[i] > height[start]:
                    start = i
                    loop = True
                    break
    return most_water
