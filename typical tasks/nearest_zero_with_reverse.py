# успешные тесты - 81248003
from typing import List, Tuple


def find_zero(arr: List[int], n: int) -> List[int]:
    distance = []
    zero_position = None
    for i, elem in enumerate(arr):
        if elem == 0:
            zero_position = i
            distance.append(0)
            continue
        if (elem != 0 and zero_position is not None):
            distance.append(i - zero_position)
        else:
            distance.append(n)
    zero_position = None
    for i, elem in reversed(list(enumerate(arr))):
        if elem == 0:
            zero_position = i
            continue
        if (elem != 0
                and zero_position is not None
                and distance[i] > zero_position - i):
            distance[i] = (zero_position - i)
    return distance


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return arr, n


arr, n = read_input()
print(" ".join(map(str, find_zero(arr, n))))
