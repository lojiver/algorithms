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
