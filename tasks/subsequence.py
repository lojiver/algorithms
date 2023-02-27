'''
Гоша любит играть в игру «Подпоследовательность»:
даны 2 строки, и нужно понять, является ли первая из них
подпоследовательностью второй. Когда строки достаточно длинные,
очень трудно получить ответ на этот вопрос, просто посмотрев на них.
Помогите Гоше написать функцию, которая решает эту задачу.
'''


def subsequence(substring, whole):
    position = -1
    for i in substring:
        position = whole.find(i, position + 1)
        if position == - 1:
            return False
    return True


if __name__ == '__main__':
    substring, whole = input(), input()
    print(subsequence(substring, whole))
