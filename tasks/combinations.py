'''
На клавиатуре старых мобильных телефонов каждой цифре
соответствовало несколько букв. Примерно так:
2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона,
без учета повторов. Напечатайте все комбинации букв,
которые можно набрать такой последовательностью нажатий.
'''


numbers_letters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def numbers_to_letters(n, combination, prefix, result=[]):
    if n == 0:
        result.append(prefix)
    else:
        numbers_to_letters(
            n - 1,
            combination[1:len(combination)],
            prefix + numbers_letters[combination[0]][0], result)
        numbers_to_letters(
            n - 1,
            combination[1:len(combination)],
            prefix + numbers_letters[combination[0]][1], result)
        numbers_to_letters(
            n - 1,
            combination[1:len(combination)],
            prefix + numbers_letters[combination[0]][2], result)
        if len(numbers_letters[combination[0]]) == 4:
            numbers_to_letters(
                n - 1,
                combination[1:len(combination)],
                prefix + numbers_letters[combination[0]][3], result)
        return result


def read_input() -> int:
    n = input()
    return n


if __name__ == '__main__':
    n = read_input()
    for value in numbers_to_letters(len(n), n, ''):
        print(value, end=' ')
