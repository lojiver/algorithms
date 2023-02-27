'''
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
'''


def check_parity(a: int, b: int, c: int) -> bool:
    del_a = a % 2
    del_b = b % 2
    del_c = c % 2
    return del_a == del_b == del_c


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


if __name__ == '__main__':
    a, b, c = map(int, input().strip().split())
    print_result(check_parity(a, b, c))
