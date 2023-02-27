'''
Метеорологическая служба вашего города решила исследовать погоду новым
способом.
Под температурой воздуха в конкретный день будем понимать
максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней,
в которые температура строго больше, чем в день до (если такой существует)
и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла
[1, 2, 5, 4, 8] градусов, то хаотичность за этот период
равна 2:в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды
за этот период.
Заметим, что если число показаний n=1, то единственный день будет хаотичным.
'''


from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return 1

    result = 0
    if temperatures[0] > temperatures[1]:
        result += 1
    if temperatures[-1] > temperatures[-2]:
        result += 1
    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            result += 1
    return result


def read_input() -> List[int]:
    _ = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


if __name__ == '__main__':
    temperatures = read_input()
    print(get_weather_randomness(temperatures))
