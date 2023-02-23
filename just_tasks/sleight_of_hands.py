# успешные тесты 81276691
from typing import List, Tuple


def calculate_score(arr: List[int], k: int) -> List[int]:
    count_numbers = [0] * 10
    result = 0
    for i in arr:
        for number in range(0, 10):
            if i == number:
                count_numbers[number] += 1

    for i in range(1, 10):
        if count_numbers[i] <= 2*k and count_numbers[i] != 0:
            result += 1
    return result


def dot_to_zero(elem):
    if elem == '.':
        return int(0)
    return int(elem)


def read_input() -> Tuple[List[str], List[str]]:
    k = int(input())
    row_1 = list(map(dot_to_zero, input().strip()))
    row_2 = list(map(dot_to_zero, input().strip()))
    row_3 = list(map(dot_to_zero, input().strip()))
    row_4 = list(map(dot_to_zero, input().strip()))
    arr = row_1 + row_2 + row_3 + row_4
    return arr, k


arr, k = read_input()
print(calculate_score(arr, k))
