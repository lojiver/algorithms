from typing import List


def merge(arr: list, lf: int, mid: int, rg: int) -> List[int]:
    left = arr[lf:mid]
    right = arr[mid:rg]
    i = j = 0
    k = lf

    while i < len(left) and j < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while i < len(left):
        arr[k] = left[i]  # перенеси оставшиеся элементы left в result
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]  # перенеси оставшиеся элементы right в result
        j += 1
        k += 1

    return arr


def merge_sort(arr, lf, rg):
    if rg - lf <= 1:  # базовый случай рекурсии
        return
    else:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected
