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
    cache = {}

    def get(idx):
        if idx not in cache:
            val = mountain_arr.get(idx)
            cache[idx] = val
        return cache[idx]

    def is_slope(s, e):
        if e - s >= 3:
            val_s, val_m1, val_m2, val_e = get(s), get(s+1), get(e-1), get(e)
            return val_s < val_m1 < val_m2 < val_e or val_s > val_m1 > val_m2 > val_e
        if e - s == 2:
            return not get(s+1) > max(get(s), get(e))
        return True

    def find_in_slope(s, e):
        if get(s) == target:
            return s
        if get(e) == target:
            return e
        if get(s) < target < get(e) or get(s) > target > get(e):
            m = int((s+e)/2)
            if m not in [s, e]:
                p = find_in_mountain(s, m)
                if p > -1:
                    return p
                p = find_in_mountain(m, e)
                if p > -1:
                    return p
        return -1

    def find_in_mountain(s, e):
        if get(s) > target and get(e) > target:
            return -1
        if get(s) == target:
            return s
        if e - s <= 2 and get(e) == target:
            return e
        m = int((s+e)/2)
        pos = find_in_slope(s, m) if is_slope(s, m) else find_in_mountain(s, m)
        if pos > 0:
            return pos
        pos = find_in_slope(m, e) if is_slope(m, e) else find_in_mountain(m, e)
        if pos > 0:
            return pos
        return -1

    return find_in_mountain(0, mountain_arr.length()-1)


def happy_number(n: int) -> bool:
    cache = set()

    def do_match(num):
        total = 0
        while num >= 10:
            i = num % 10
            num = int(num/10)
            total += i**2
        total += num**2
        return total

    m = n
    while m not in cache:
        if m == 1:
            return True
        cache.add(m)
        m = do_match(m)
    return False


def jump_game_ii(nums: List[int]) -> int:
    if len(nums) <= 1:
        return 0
    cache = {}
    for idx in range(-1, -1*len(nums)-1, -1):
        num = nums[idx]
        if num == 0:
            continue
        min_step = None
        for i in range(num, 0, -1):
            if i >= -1-idx:
                min_step = 1
                break
            j = idx + i
            if -1*len(nums) < j < -1 and j in cache:
                min_step = min(min_step, 1+cache[j]) if min_step is not None else 1+cache[j]
        if min_step is not None:
            cache[idx] = min_step
    return cache[-1*len(nums)]

