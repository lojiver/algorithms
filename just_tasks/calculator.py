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


print(calculate(read_input()))
