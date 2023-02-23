def bubble_sort(arr):
    flag = 1
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if flag == 1:
            print(' '.join(list(map(str, arr))))
            flag = 0


def read_input():
    input()
    arr = list(map(int, input().strip().split()))
    return arr


if __name__ == '__main__':
    bubble_sort(read_input())
