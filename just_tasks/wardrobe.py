def sort_wardrobe(arr):
    zeros = 0
    ones = 0
    twos = 0
    for value in arr:
        if value == 0:
            zeros += 1
        if value == 1:
            ones += 1
        if value == 2:
            twos += 1
    print('0 ' * zeros + '1 ' * ones + '2 ' * twos)


if __name__ == '__main__':
    input()
    arr = list(map(int, input().strip().split()))
    sort_wardrobe(arr)
