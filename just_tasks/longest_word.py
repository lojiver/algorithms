def get_longest_word(line: list) -> str:
    longest_length = 0
    longest_word = ''
    for word in line:
        length = len(word)
        if length > longest_length:
            longest_length = length
            longest_word = word
    return longest_word


def read_input() -> list:
    _ = input()
    line = list(map(str, input().strip().split()))
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
