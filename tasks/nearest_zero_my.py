'''
Тимофей ищет место, чтобы построить себе дом.
Улица, на которой он хочет жить, имеет длину n,
то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.
Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего
пустого участка. Если участок пустой, эта величина будет равна нулю —
расстояние до самого себя.
Помогите Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались
в том порядке, в котором строились, поэтому их номера на карте никак
не упорядочены. Пустые участки обозначены нулями.
'''

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


if __name__ == '__main__':
    arr, n = read_input()
    print(" ".join(map(str, find_zero(arr, n))))
