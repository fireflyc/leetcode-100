from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    def search(row, column):
        if not grid[row][column]:
            return set()
        area, new_found = {(row, column)}, [(row, column)]
        while new_found:
            pos, new_found = new_found[0], new_found[1:]
            for r, c in [(pos[0]-1, pos[1]+0), (pos[0]+1, pos[1]+0), (pos[0]+0, pos[1]-1), (pos[0]+0, pos[1]+1)]:
                if 0 <= r < len(grid) and 0 <= c < len(grid[r]) and grid[r][c] and (r, c) not in area:
                    area.add((r, c))
                    new_found.append((r, c))
        return area

    max_area, searched = 0, set()
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if (r, c) not in searched:
                s = search(r, c)
                max_area = max(len(s), max_area)
                searched.update(s)
    return max_area


def escape_a_large_maze(blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    if not blocked:
        return True
    max_size, traverse_limit = 10**6, int((len(blocked)**2))
    blocked = set([tuple(b) for b in blocked])

    def bfs(r, c, package, queue, aim):
        if (r, c) == tuple(aim):
            return True
        if (r, c) not in blocked and (r, c) not in package:
            package.add((r, c))
            queue.extend([(x, y) for x, y in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)] if 0 <= x < max_size and 0 <= y < max_size])
        return False

    source_traversed, source_queue = set(), [tuple(source)]
    target_traversed, target_queue = set(), [tuple(target)]
    while source_queue and target_queue:
        if len(source_traversed) > traverse_limit and len(target_traversed) > traverse_limit:
            return True
        source_one, source_queue = source_queue[0], source_queue[1:]
        target_one, target_queue = target_queue[0], target_queue[1:]
        rslt = bfs(source_one[0], source_one[1], source_traversed, source_queue, target) \
               or bfs(target_one[0], target_one[1], target_traversed, target_queue, source)
        if rslt:
            return True
    return False


def word_search(board: List[List[str]], word: str) -> bool:

    def bfs(r, c, target, traversed):
        if not (0 <= r < len(board) and 0 <= c < len(board[r])) or (r, c) in traversed:
            return False
        if not target:
            return True
        traversed.add((r, c))
        if board[r][c] != target[0]:
            return False
        if board[r][c] == target:
            return True
        return bfs(r-1, c, target[1:], traversed.copy()) or bfs(r+1, c, target[1:], traversed.copy()) \
            or bfs(r, c-1, target[1:], traversed.copy()) or bfs(r, c+1, target[1:], traversed.copy())

    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            found = bfs(r, c, word, set())
            if found:
                return True
    return False


def check_if_there_is_a_valid_path_in_a_grid(grid: List[List[int]]) -> bool:
    cell = {
        1: {"left", "right"}, 2: {"top", "down"}, 3: {"left", "down"},
        4: {"down", "right"}, 5: {"top", "left"}, 6: {"top", "right"}
    }
    enter_direction = {(1, 0): "top", (-1, 0): "down", (0, -1): "right", (0, 1): "left"}
    exit_direction = {"left": (0, -1), "right": (0, 1), "top": (-1, 0), "down": (1, 0)}
    traversed, queue = set(), [(0, 0)]

    while queue:
        block, queue = queue[0], queue[1:]
        if block == (len(grid)-1, len(grid[0])-1):
            return True
        cell_num = grid[block[0]][block[1]]
        for d in cell[cell_num]:
            exit_from = exit_direction[d]
            coord = (block[0]+exit_from[0], block[1]+exit_from[1])
            if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]):
                coord_num = grid[coord[0]][coord[1]]
                enter_from = enter_direction[exit_from]
                if enter_from in cell[coord_num] and coord not in traversed:
                    queue.append(coord)
        traversed.add(block)
    return False


def as_far_from_land_as_possible(grid: List[List[int]]) -> int:
    grid_sum = sum([sum(g) for g in grid])
    if grid_sum in [0, len(grid)*len(grid[0])]:
        return -1

    def search(row, col):
        if grid[row][col]:
            return 0
        for md in range(1, len(grid)+len(grid[0])):
            for i in range(-md, md+1):
                j = md - abs(i)
                for coord in [(row+i, col+j), (row+i, col-j)]:
                    if 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0]) and grid[coord[0]][coord[1]]:
                        return md
        return 0

    max_distance = 0
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            d = search(r, c)
            max_distance = max(d, max_distance)
    return max_distance


def generate_parentheses(n: int) -> List[str]:
    left_bracket, right_bracket = "(", ")"
    choices = [left_bracket]

    while len(choices[0]) < n*2:
        tmp = []
        for c in choices:
            left_num, right_num = c.count(left_bracket), c.count(right_bracket)
            if left_num < n:
                tmp.append(c+left_bracket)
            if right_num < left_num and right_num < n:
                tmp.append(c+right_bracket)
        choices = tmp
    return choices


def zero_one_matrix(mat: List[List[int]]) -> List[List[int]]:
    def zero_one_distance(row, col):
        if mat[row][col] == 0:
            return 0
        for distance in range(1, len(mat[0])+len(mat)):
            for i in range(-1*distance, distance+1):
                for j in [distance - abs(i), abs(i) - distance]:
                    ri, cj = row+i, col+j
                    if 0 <= ri < len(mat) and 0 <= cj < len(mat[0]):
                        if mat[ri][cj] == 0:
                            return distance

    result = [[None for j in range(0, len(mat[0]))] for i in range(0, len(mat))]
    for r in range(0, len(mat)):
        for c in range(0, len(mat[0])):
            result[r][c] = zero_one_distance(r, c)
    return result


def number_of_islands(grid: List[List[str]]) -> int:

    def mark_island(row, col):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if grid[row][col] == "1":
                grid[row][col] = "-1"
                mark_island(row-1, col)
                mark_island(row+1, col)
                mark_island(row, col-1)
                mark_island(row, col+1)

    amount = 0
    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            cell = grid[r][c]
            if cell == "1":
                mark_island(r, c)
                amount += 1
    return amount


def permutations(nums: List[int]) -> List[List[int]]:
    all_permutation = []
    choices = [[num] for num in nums]
    while choices:
        choice, choices = choices[0], choices[1:]
        if len(choice) == len(nums):
            all_permutation.append(choice)
        else:
            remain = set(nums) - set(choice)
            choices.extend([choice + [item] for item in remain])
    return all_permutation
