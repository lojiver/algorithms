# успешные тесты 81254657
from typing import List, Tuple


def find_zero(arr: List[int], n: int) -> List[int]:
    result = []
    zero_positions = []
    for i in range(n):
        if arr[i] == 0:
            zero_positions.append(i)

    for number in range(0, zero_positions[0]):
        result.append(zero_positions[0] - number)

    for i in range(len(zero_positions) - 1):
        prev_zero, next_zero = zero_positions[i], zero_positions[i + 1]
        for number in range(prev_zero, next_zero):
            result.append(min(
                abs(prev_zero - number),
                abs(next_zero - number)))

    for number in range(zero_positions[-1], len(arr)):
        result.append(abs(zero_positions[-1] - number))

    return result


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return arr, n


arr, n = read_input()
print(" ".join(map(str, find_zero(arr, n))))
