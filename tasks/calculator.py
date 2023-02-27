'''
Задание связано с обратной польской нотацией.
Она используется для парсинга арифметических выражений.
Еще её иногда называют постфиксной нотацией.
В постфиксной нотации операнды расположены перед знаками операций.
Пример 1:
3 4 +
означает 3 + 4 и равно 7

Пример 2:
12 5 /
Так как деление целочисленное, то в результате получим 2.

Пример 3:
10 2 4 * -
означает 10 - 2 * 4 и равно 2

Разберём последний пример подробнее:
Знак * стоит сразу после чисел 2 и 4, значит к ним нужно применить операцию,
которую этот знак обозначает, то есть перемножить эти два числа.
В результате получим 8. После этого выражение приобретёт вид:
10 8 -
Операцию «минус» нужно применить к двум идущим перед ней числам,
то есть 10 и 8. В итоге получаем 2.
Рассмотрим алгоритм более подробно. Для его реализации будем использовать стек.
'''
# успешная попытка 81981299


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def calculate(arr):
    dictionary = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }
    stack = Stack()
    for value in arr:
        if isinstance(value, int):
            stack.push(int(value))
        else:
            stack.push(dictionary[value](stack.pop(), stack.pop()))

    return stack.pop()


def int_or_str(elem):
    if elem in ['+', '-', '*', '/']:
        return elem
    return int(elem)


def read_input() -> str:
    arr = list(map(int_or_str, input().strip().split()))
    return arr


if __name__ == '__main__':
    print(calculate(read_input()))
