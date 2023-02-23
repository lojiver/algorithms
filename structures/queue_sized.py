class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size_attr = 0

    def is_empty(self):
        return self.size_attr == 0

    def push(self, x):
        if self.size_attr == self.max_size:
            return print('error')
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size
        self.size_attr += 1

    def pop(self):
        if self.is_empty():
            return 'None'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size_attr -= 1
        return x

    def peek(self):
        return self.queue[self.head]

    def size(self):
        return self.size_attr


def read_input():
    n = int(input())
    m = int(input())
    queue = MyQueueSized(m)
    i = 0
    while i < n:
        cmd, *value = input().strip().split()
        if value:
            getattr(queue, cmd)(int(value[0]))
        else:
            print(getattr(queue, cmd)())
        i += 1


if __name__ == '__main__':
    read_input()
