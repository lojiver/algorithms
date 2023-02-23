# успешная попытка на контесте 82840368


def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end - 1
    while True:
        while (left <= right and arr[right] > pivot):
            right -= 1
        while (left <= right and arr[left] < pivot):
            left += 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            arr[start], arr[right] = arr[right], arr[start]
            return right


def quicksort(arr, start, end):
    if (end - start) > 1:
        p = partition(arr, start, end)
        quicksort(arr, start, p)
        quicksort(arr, p + 1, end)


def transformation(competitors):
    competitors[1] = - int(competitors[1])
    competitors[2] = int(competitors[2])

    return [competitors[1], competitors[2], competitors[0]]


def read_input():
    n = int(input())
    result = []
    i = 0
    while i < n:
        result.append(transformation(input().split()))
        i += 1
    return result


if __name__ == '__main__':
    arr = read_input()
    quicksort(arr, 0, len(arr))
    for value in arr:
        print(value[2])
