# успешные тесты - 81253053
from typing import List, Tuple


def find_zero(arr: List[int], n: int) -> List[int]:
    result = [0] * len(arr)
    zero_list = [i for i in range(n) if arr[i] == 0]

    for house in range(0, zero_list[0] + 1):
        result[house] = zero_list[0] - house

    for pos in range(len(zero_list) - 1):
        zero_1, zero_2 = zero_list[pos], zero_list[pos + 1]
        for house in range(zero_1, zero_2):
            result[house] = min(house - zero_1, zero_2 - house)

    for house in range(zero_list[-1], len(arr)):
        result[house] = house - zero_list[-1]

    return result


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return arr, n


arr, n = read_input()
print(" ".join(map(str, find_zero(arr, n))))
