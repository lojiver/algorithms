def biggest_number(arr):
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i
        while j > 0 and int(
                item_to_insert + arr[j-1]) > int(arr[j-1] + item_to_insert):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item_to_insert
    return ''.join(arr)


def read_input():
    input()
    arr = input().strip().split()
    return arr


if __name__ == '__main__':
    print(biggest_number(read_input()))
