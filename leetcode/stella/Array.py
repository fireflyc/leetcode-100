from typing import List


def find_the_distance_value_between_two_arrays(arr1: List[int], arr2: List[int], d: int) -> int:
    total = len(arr1)
    for n1 in arr1:
        for n2 in arr2:
            if abs(n1-n2) <= d:
                total -= 1
                break
    return total


def rotate_matrix_lcci(matrix: List[List[int]]) -> None:
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0, len(matrix)):
        for j in range(0, int(len(matrix[0])/2)):
            matrix[i][j], matrix[i][len(matrix[0])-1-j] = matrix[i][len(matrix[0])-1-j], matrix[i][j]
