'''
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются
одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.
'''


import string


def is_palindrome(pal: str) -> bool:
    length = len(pal) // 2
    for i in range(0, length):
        if pal[i] != pal[-(i+1)]:
            return False
    return True


def lower_del_punctuation_and_spaces(elem):
    if elem == ' ' or elem in string.punctuation:
        return ''
    return elem.lower()


def read_input() -> str:
    pal = ''.join(map(lower_del_punctuation_and_spaces, input().strip()))
    return pal


if __name__ == '__main__':
    pal = read_input()
    print(is_palindrome(pal))
