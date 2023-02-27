'''
Рита решила оставить у себя одежду только трёх цветов: розового,
жёлтого и малинового. После того как вещи других расцветок были убраны,
Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого,
и в конце —– малинового. Помогите Рите справиться с этой задачей.
Примечание: попробуйте решить задачу за один проход по массиву!
'''


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
