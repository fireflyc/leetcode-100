from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    def search(row, column):
        if not grid[row][column]:
            return set()
        area = {(row, column)}
        new_found = [(row, column)]
        while new_found:
            pos = new_found[0]
            new_found = new_found[1:]
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
    pass

