def generate_bracket_sequence(i, n1, n2, prefix):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            generate_bracket_sequence(i + 1, n1 - 1, n2, prefix + '(')
        if (i > 0 and n2 > 0):
            generate_bracket_sequence(i - 1, n1, n2 - 1, prefix + ')')


def read_input() -> int:
    n = int(input())
    return n


if __name__ == '__main__':
    n = read_input()
    generate_bracket_sequence(1, n - 1, n, '(')
