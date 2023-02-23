from typing import List, Tuple


def binary_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[0] >= x:
        return 1
    if arr[mid] >= x > arr[mid - 1]:
        return mid + 1
    elif x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def calculate(arr, cost):
    first_bicycle = binary_search(arr, cost, 0, len(arr))
    second_bicycle = binary_search(arr, cost * 2, first_bicycle, len(arr))
    return print(first_bicycle, second_bicycle)


def read_input() -> Tuple[List[int], int]:
    input()
    arr = list(map(int, input().strip().split()))
    cost = int(input())
    return arr, cost


if __name__ == '__main__':
    arr, cost = read_input()
    calculate(arr, cost)
