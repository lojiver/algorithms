'''
Дана скобочная последовательность. Нужно определить, правильная ли она.
Будем придерживаться такого определения:
пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа, –—
правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева или справа
правильной скобочной последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход
скобочную последовательность и возвращает True, если последовательность
правильная, а иначе False.
'''


D = {
    '(': ')',
    '{': '}',
    '[': ']'
}


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def define_brackets(str) -> bool:
    s = Stack()
    for x in str:
        if x in D.keys():
            s.push(x)
        elif not s.isEmpty() and D[s.peek()] == x:
            s.pop()
        else:
            s.push(x)
            break
    return s.isEmpty()


def read_input() -> str:
    str = input()
    return str


if __name__ == '__main__':
    print(define_brackets(read_input()))
