class StackMax:
    def __init__(self):
        self.items = []
        self.max_items = [None]

    def push(self, item):
        self.items.append(item)
        if self.max_items[-1] is None or item >= self.max_items[-1]:
            self.max_items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return print('error')
        if self.max_items[-1] == self.items[-1]:
            self.max_items.pop()
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            return print('None')
        return print(self.max_items[-1])


def read_input():
    n = int(input())
    stack = StackMax()
    i = 0
    while i < n:
        cmd, *value = input().strip().split()
        if value:
            getattr(stack, cmd)(int(value[0]))
        else:
            getattr(stack, cmd)()
        i += 1


if __name__ == '__main__':
    read_input()
