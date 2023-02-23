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


pal = read_input()
print(is_palindrome(pal))
