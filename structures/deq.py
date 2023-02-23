# успешная попытка 81980575

class Deq:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, x):
        if self.size == self.max_n:
            return print('error')
        self.tail = (self.tail + 1) % self.max_n
        self.queue[self.tail] = x
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.tail = (self.tail - 1) % self.max_n
        self.size -= 1
        return x

    def push_front(self, x):
        if self.size == self.max_n:
            return print('error')
        self.head = (self.head - 1) % self.max_n
        self.queue[self.head] = x
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            return 'error'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


def read_input():
    n = int(input())
    m = int(input())
    deq = Deq(m)
    i = 0
    while i < n:
        cmd, *value = input().strip().split()
        if value:
            getattr(deq, cmd)(int(value[0]))
        else:
            print(getattr(deq, cmd)())
        i += 1


if __name__ == '__main__':
    read_input()
