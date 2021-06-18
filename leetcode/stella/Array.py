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
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] >= gap:
            reachable = True
            gap = 1
        if nums[i] == 0 or (nums[i] < gap and not reachable):
            reachable = False
            gap += 1
    return reachable


def container_with_most_water(height: List[int]) -> int:
    most_water = 0
    start, end, loop = 0, len(height) - 1, True
    while start < end and loop:
        loop = False
        most_water = max(min(height[start], height[end]) * (end - start), most_water)
        if height[start] >= height[end]:
            for i in range(end - 1, start, -1):
                if height[i] > height[end]:
                    end = i
                    loop = True
                    break
        elif height[end] > height[start]:
            for i in range(start + 1, end):
                if height[i] > height[start]:
                    start = i
                    loop = True
                    break
    return most_water


def count_number_of_nice_subarrays(nums: List[int], k: int) -> int:
    evens_between = []
    count_evens = 0
    for n in nums:
        if n % 2:
            evens_between.append(count_evens)
            count_evens = 0
        else:
            count_evens += 1
    evens_between.append(count_evens)
    if k > len(evens_between) - 1:
        return 0
    count = 0
    for i in range(0, len(evens_between) - k):
        count += (evens_between[i] + 1) * (evens_between[i + k] + 1)
    return count


def search_in_rotated_sorted_array(nums: List[int], target: int) -> int:
    factor = 1 if target >= nums[0] else -1
    idx = 0 if factor > 0 else -1
    while 0 <= idx < len(nums) or -1 * len(nums) <= idx < 0:
        if nums[idx] != target:
            if (factor < 0 and idx + factor >= -1 * len(nums) and nums[idx + factor] < nums[idx]) or \
                    (factor > 0 and idx + factor < len(nums) and nums[idx + factor] > nums[idx]):
                idx += factor
            else:
                return -1
        else:
            return idx if factor > 0 else len(nums) + idx
    return -1


class MountainArray:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


def find_in_mountain_array(target: int, mountain_arr: MountainArray) -> int:
    pass
