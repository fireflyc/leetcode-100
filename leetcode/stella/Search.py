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
    traversed = set()
    queue = [(0, 0)]

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






