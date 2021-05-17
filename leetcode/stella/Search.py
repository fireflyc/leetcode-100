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

    max_row, max_col = 10**6, 10**6
    blocked, traversed, track = set([tuple(b) for b in blocked]), set(), [tuple(source)]

    def next_step(cur_pos):
        relative_pos = [(1, 0) if target[0] > cur_pos[0] else (-1, 0), (0, 1) if target[1] > cur_pos[1] else (0, -1)]
        for r, c in relative_pos:
            abs_pos = (cur_pos[0] + r, cur_pos[1] + c)
            if 0 <= abs_pos[1] <= max_col and 0 <= abs_pos[0] <= max_row and abs_pos not in traversed and abs_pos not in blocked:
                return abs_pos

    while track:
        next_pos = next_step(track[-1])
        if not next_pos:
            track.pop()
        elif next_pos == tuple(target):
            return True
        else:
            track.append(next_pos)
            traversed.add(next_pos)
    return False

